# Generated by Django 4.1.7 on 2023-03-29 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='bio',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]