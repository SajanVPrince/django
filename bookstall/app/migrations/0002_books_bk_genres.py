# Generated by Django 5.1.2 on 2024-11-09 09:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='bk_genres',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
