# Generated by Django 5.1.2 on 2024-11-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='abcclg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('about', models.TextField()),
                ('mission', models.TextField()),
                ('vision', models.TextField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('course', models.TextField()),
                ('feature', models.TextField()),
            ],
        ),
    ]