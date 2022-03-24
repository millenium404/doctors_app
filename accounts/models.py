from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    is_doctor = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'
