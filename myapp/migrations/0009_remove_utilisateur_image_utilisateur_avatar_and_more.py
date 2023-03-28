# Generated by Django 4.1.7 on 2023-03-28 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_profile_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='image',
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='avatar',
            field=models.ImageField(default='Tortuga.png', upload_to='profile_images'),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='bio',
            field=models.TextField(default=0),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
