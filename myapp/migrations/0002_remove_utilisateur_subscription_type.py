# Generated by Django 4.2 on 2023-05-08 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='subscription_type',
        ),
    ]
