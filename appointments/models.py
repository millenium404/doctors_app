from django.db import models
from django.contrib.auth.models import User
from doctors.models import Doctor

# Create your models here.
class Appointment(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE)
    user_id = models.IntegerField(blank=True, null=True)
    hour = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.doctor} - {self.hour}'
