# Generated by Django 3.2.12 on 2022-03-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
    ]
