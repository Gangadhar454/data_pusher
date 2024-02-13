from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Destination
from .serializers import (
    DestinationSerializer,
    DestinationCreationSerializer,
    DestinationModificationSerializer
)


class DestinationView(APIView):

    def get(self, request):
        try:
            account_id = request.GET.get('account_id', None)
            if not account_id:
                return Response({
                    "status": False,
                    "message": "account id not present"
                })
            destinations = Destination.objects.filter(account_id=account_id)
            destination_details = DestinationSerializer(destinations, many=True).data
            return Response(
                {
                    'status': True,
                    'data': destination_details
                },
                status=200
            )
        except Exception as e:
            return Response(
                {
                    'status': False,
                    "message": "No results found"
                }
            )

    def post(self, request):
        try:
            serializer = DestinationCreationSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    "status": False,
                    "message": serializer.errors
                    },
                    status=200
                )
            data = request.data
            Destination.objects.create(**data)
            return Response({
                "status": True,
                "message": "Destination Created Successfully"
            })
        except Exception as e:
            return Response(
                {
                    "status": False,
                    "message": "Operation Failed"
                }
            )

    def delete(self, request):
        try:
            data = request.data
            requested_destination_id = data["destination_id"]
            try:
                Destination.objects.get(id=requested_destination_id).delete()
            except Destination.DoesNotExist:
                return Response(
                    {
                        "status": False,
                        "message": "Invalid Details"
                    }
                )
            return Response({
                "status": True,
                "message": "Deleted Successfully"
            })
        except Exception as e:
            return Response(
                {
                    "status": False,
                    "message": "Operation Failed"
                }
            )

    def patch(self, request):
        try:
            serializer = DestinationModificationSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    "status": False,
                    "message": serializer.errors
                    },
                    status=200
                )
            data = request.data
            requested_destination_id = data.pop("destination_id")
            try:
                destination = Destination.objects.get(
                    id=requested_destination_id,
                )
                if "url" in data:
                    destination.url = data['url']
                if "http_method" in data:
                    destination.http_method = data['http_method']
                if "headers" in data:
                    destination.headers = data["headers"]
                destination.save()
            except Destination.DoesNotExist:
                return Response(
                    {
                        "status": False,
                        "message": "Invalid Details"
                    }
                )
            return Response({
                "status": True,
                "message": "Updated Successfully"
            })
        except Exception as e:
            return Response(
                {
                    "status": False,
                    "message": "Operation Failed"
                }
            )
