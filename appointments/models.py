from django.db import models
from datetime import date

from patients.models import Patient
from doctors.models import Doctor


class Appointment(models.Model):
    title = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=250, default="")
    created_at = models.DateField(default=date.today)
    doctor = models.ForeignKey(Doctor, models.CASCADE)
    patient = models.ForeignKey(Patient, models.CASCADE)
    appointment_date = models.DateField(default=date.today)
