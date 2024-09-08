# patients/models.py

from django.contrib.auth.models import User
from django.db import models

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)