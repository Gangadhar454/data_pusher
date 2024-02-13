from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Account
from .serializers import (
    AccountSerializer,
    AccountCreationSerializer,
    AccountDeletionSerializer,
    AccountModificationSerializer
)

class AccountView(APIView):

    def get(self, request):
        try:
            account_id = request.GET.get('account_id', None)
            if account_id:
                account = Account.objects.get(account_id=account_id)
                account_details = AccountSerializer(account).data
            else:
                accounts = Account.objects.all()
                account_details = AccountSerializer(accounts, many=True).data
            return Response(
                {
                    'status': True,
                    'data': account_details
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
            serializer = AccountCreationSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    "status": False,
                    "message": serializer.errors
                    },
                    status=200
                )
            Account.objects.create(**request.data)
            return Response({
                "status": True,
                "message": "Account Created Successfully"
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
            serializer = AccountDeletionSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    "status": False,
                    "message": serializer.errors
                    },
                    status=200
                )
            data = request.data
            requested_account_id = data["account_id"]
            requested_secret_token = data["secret_token"]
            try:
                Account.objects.get(
                    account_id=requested_account_id,
                    secret_token=requested_secret_token
                ).delete()
            except Account.DoesNotExist:
                return Response(
                    {
                        "status": False,
                        "message": "Invalid Details"
                    }
                )
            # account.delete()
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
            serializer = AccountModificationSerializer(data=request.data)
            if not serializer.is_valid():
                return Response({
                    "status": False,
                    "message": serializer.errors
                    },
                    status=200
                )
            data = request.data
            requested_account_id = data.pop("account_id")
            requested_secret_token = data.pop("secret_token")
            try:
                account = Account.objects.get(
                    account_id=requested_account_id,
                    secret_token=requested_secret_token
                )
                if "account_name" in data:
                    account.account_name = data['account_name']
                if "website" in data:
                    account.website = data['website']
                if "email" in data:
                    account.email = data["email"]
                account.save()
            except Account.DoesNotExist:
                return Response(
                    {
                        "status": False,
                        "message": "Invalid Details"
                    }
                )
            # account.delete()
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