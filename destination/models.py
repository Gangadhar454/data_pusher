from django.db import models
from account.models import Account


class Destination(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    url = models.URLField()
    http_method_choices = [
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
    ]
    http_method = models.CharField(max_length=6, choices=http_method_choices)
    headers = models.JSONField()

