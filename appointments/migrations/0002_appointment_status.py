# Generated by Django 3.2.12 on 2022-04-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
