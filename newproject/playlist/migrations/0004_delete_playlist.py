# Generated by Django 3.2.9 on 2021-11-07 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pleer', '0003_auto_20211029_1643'),
        ('playlist', '0003_playlist'),
    ]

    operations = [
        migrations.DeleteModel(
            name='playlist',
        ),
    ]
