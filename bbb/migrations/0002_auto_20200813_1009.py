# Generated by Django 2.2.15 on 2020-08-13 08:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='moderators',
            field=models.ManyToManyField(blank=True, related_name='moderating', to=settings.AUTH_USER_MODEL),
        ),
    ]