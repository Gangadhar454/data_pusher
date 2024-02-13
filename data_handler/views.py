from rest_framework.views import APIView
from rest_framework.response import Response
from worker.tasks import send_data_to_destinations
from account.models import Account
import json

class SendDataToDestinations(APIView):

    def validate_account_details(self, account_id, secret_token):
        try:
            account = Account.objects.get(account_id=account_id)
            if account.secret_token != secret_token:
                return Response({
                    "status": False,
                    "message": "Un Authenticate"
                })
        except Account.DoesNotExist:
            return Response({
                "status": False,
                "message": "Invalid Data"
            })

    def post(self, request):
        request_data = request.data
        if (
                "account_id" not in request_data
                or
                "secret_token" not in request_data
        ):
            return Response({
                "status": False,
                "message": "Invalid Data"
            })
        account_id = request_data['account_id']
        secret_token = request_data['secret_token']
        data = request_data['data']
        validation_response = self.validate_account_details(account_id, secret_token)
        if validation_response:
            return validation_response
        send_data_to_destinations.apply_async(
            args=[account_id, data]
        )
        return Response({
            "status": True
        })
    
    def get(self, request):
        request_data = request.GET
        if (
                "account_id" not in request_data
                or
                "secret_token" not in request_data
        ):
            return Response({
                "status": False,
                "message": "Invalid Data"
            })
        account_id = request_data['account_id']
        secret_token = request_data['secret_token']
        data = request_data['data']
        validation_response = self.validate_account_details(account_id, secret_token)
        if validation_response:
            return validation_response
        send_data_to_destinations.apply_async(
            args=[account_id, data]
        )
        return Response({
            "status": True
        })