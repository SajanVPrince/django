from django.db import models

# Create your models here.
class Phone(models.Model):
    name=models.TextField()
    email=models.TextField()
    place=models.TextField()
    phone=models.TextField()
    whatsapp=models.TextField()
    