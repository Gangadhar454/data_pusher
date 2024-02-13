from data_pusher.celery import app
from destination.models import Destination
import concurrent.futures
from rest_framework.response import Response
import requests
from urllib.parse import urlencode


@app.task(name="send_data_to_destinations", bind=True)
def send_data_to_destinations(self, account_id, data):
    destinations: Destination = Destination.objects.filter(account_id=account_id)
    
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(destinations)) as executor:
            futures = [executor.submit(send_request, destination, data) for destination in destinations]
            results = [future.result() for future in concurrent.futures.as_completed(futures)]
            print("results ->", results)
    except Exception as e:
        import traceback
        traceback.print_exc()

def send_request(destination: Destination, data):
    url = destination.url
    headers = destination.headers
    http_method = destination.http_method
    if http_method == 'GET':
        query_string = urlencode(data) 
        final_url = f"{url}?{query_string}"
        response = requests.get(final_url, headers=headers)
    elif http_method == "PUT":
        response = requests.put(url, json=data, headers=headers)
    elif http_method == "PATCH":
        response = requests.patch(url, json=data, headers=headers)
    elif http_method == "POST":
        response = requests.post(url, json=data, headers=headers)
    elif http_method == "DELETE":
        response = requests.delete(url, json=data, headers=headers)
    return response.status_code