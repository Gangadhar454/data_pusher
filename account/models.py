import random
import string
from django.db import models

def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))

class Account(models.Model):
    email = models.EmailField(unique=True)
    account_id = models.AutoField(primary_key=True, unique=True)
    account_name = models.CharField(max_length=100)
    secret_token = models.CharField(max_length=32, default=generate_token)
    website = models.URLField(blank=True, null=True)