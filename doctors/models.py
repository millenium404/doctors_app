from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image

# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital = models.CharField(max_length=100, blank=True, null=True)
    practice_name = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    nzok = models.BooleanField(default=False)
    children = models.BooleanField(default=False)
    price = models.FloatField(blank=True, null=True)
    map_url = models.CharField(max_length=250, blank=True, null=True)
    active = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='')

    def save(self, **kwargs):
        super().save()
        im = Image.open(self.image.path)
        min_size = 256
        x, y = im.size
        size = max(min_size, x, y)
        new_im = Image.new('RGB', (size, size))
        new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
        if new_im.height > 200 or img.width > 200:
            output_size = (200, 200)
            new_im.thumbnail(output_size)
            new_im.save(self.image.path)


@receiver(post_save, sender=User)
def create_doctor(sender, instance, created, **kwargs):
    if created:
        Doctor.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_doctor(sender, instance, **kwargs):
    instance.doctor.save()
