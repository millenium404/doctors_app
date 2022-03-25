from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    is_doctor = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} - {self.user.username} Profile'
