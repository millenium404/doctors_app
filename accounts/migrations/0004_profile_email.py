# Generated by Django 3.2.12 on 2022-03-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220324_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
