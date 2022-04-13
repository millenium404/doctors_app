from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image


class DoctorQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == '':
            return self.none()
        query = query.title()
        print(f"""
        Последно търсене за:
                    *** {query} ***
                    """)
        lookups = Q(practice_name__icontains=query) | Q(department__icontains=query) | Q(city__icontains=query)
        return self.filter(lookups)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return DoctorQuerySet(self.model, using=self.db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)


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

    objects = ArticleManager()

    def __str__(self):
        return f'{self.id} - {self.practice_name}'

    def active_doctors():
        object = Doctor.objects.filter(~Q(practice_name=None))
        return object

    def save(self, **kwargs):
        super().save()
        im = Image.open(self.image.path)
        min_size = 256
        x, y = im.size
        size = max(min_size, x, y)
        new_im = Image.new('RGB', (size, size))
        new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
        if new_im.height > 600 or new_im.width > 600:
            output_size = (600, 600)
            new_im.thumbnail(output_size)
            new_im.save(self.image.path)


@receiver(post_save, sender=User)
def create_doctor(sender, instance, created, **kwargs):
    if created:
        Doctor.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_doctor(sender, instance, **kwargs):
    instance.doctor.save()
