# Generated by Django 3.0.8 on 2020-08-17 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbb', '0009_room_yolomode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='yolomode',
            field=models.BooleanField(default=False, verbose_name='YOLO'),
        ),
    ]
