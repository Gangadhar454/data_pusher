from rest_framework import serializers
from .models import Destination


class DestinationSerializer(serializers.ModelSerializer[Destination]):
    class Meta:
        model = Destination
        fields = '__all__'

class DestinationCreationSerializer(serializers.Serializer):
    account_id = serializers.IntegerField()
    url = serializers.URLField()
    http_method_choices = [
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
    ]
    http_method = serializers.ChoiceField(choices=http_method_choices)
    headers = serializers.JSONField()

class DestinationModificationSerializer(serializers.Serializer):
    destination_id = serializers.IntegerField(required=True)
    url = serializers.URLField(required=False)
    http_method_choices = [
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
    ]
    http_method = serializers.ChoiceField(choices=http_method_choices, required=False)
    headers = serializers.JSONField(required=False)