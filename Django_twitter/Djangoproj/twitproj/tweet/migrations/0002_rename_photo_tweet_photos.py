# Generated by Django 5.1.6 on 2025-02-26 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='photo',
            new_name='photos',
        ),
    ]
