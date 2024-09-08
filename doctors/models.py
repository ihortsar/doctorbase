from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    SPECIALITY_CHOICES = [
        ("allgemeinedizin", "Allgemeinedizin"),
        ("radiologe", "Radiologe"),
        ("hautarzt", "Hautarzt"),
    ]

    TITLE_CHOICES = [
        ("dr", "Dr."),
        ("prof_dr.", "Prof. Dr."),
        ("dr_rer_nat", "Dr. rer. nat"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20, choices=TITLE_CHOICES)
    speciality = models.CharField(max_length=50, choices=SPECIALITY_CHOICES)
    name = models.CharField(max_length=100, null=True)