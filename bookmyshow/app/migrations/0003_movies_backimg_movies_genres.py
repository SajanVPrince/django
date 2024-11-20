# Generated by Django 5.1.2 on 2024-11-20 03:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_movies_lang'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='backimg',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movies',
            name='genres',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]