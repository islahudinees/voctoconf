# Generated by Django 2.2.15 on 2020-08-13 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbb', '0002_auto_20200813_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('running', models.BooleanField()),
                ('moderators', models.IntegerField()),
                ('attendees', models.IntegerField()),
                ('presenter', models.CharField(max_length=100)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='bbb.Room')),
            ],
        ),
    ]
