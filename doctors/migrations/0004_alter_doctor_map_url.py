# Generated by Django 3.2.12 on 2022-03-25 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_alter_doctor_map_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='map_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]