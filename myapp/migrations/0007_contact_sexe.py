# Generated by Django 4.2 on 2023-06-03 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_post_categorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Sexe',
            field=models.CharField(choices=[('femme', 'Femme'), ('homme', 'Homme'), ('autre', 'Autre')], default='homme', max_length=30, null=True),
        ),
    ]
