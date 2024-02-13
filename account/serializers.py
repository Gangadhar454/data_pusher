from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer[Account]):
    class Meta:
        model = Account
        fields = '__all__'

class AccountCreationSerializer(serializers.Serializer):
    account_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    website = serializers.URLField(required=False)

class AccountDeletionSerializer(serializers.Serializer):
    account_id = serializers.IntegerField(required=True)
    secret_token = serializers.CharField(required=True)

class AccountModificationSerializer(serializers.Serializer):
    account_id = serializers.IntegerField(required=True)
    secret_token = serializers.CharField(required=True)
    account_name = serializers.CharField(required=False)
    website = serializers.CharField(required=False)
    email = serializers.CharField(required=False)