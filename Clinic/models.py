from django.db import models


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)

    def __str__(self):
        return self.doctor_name
