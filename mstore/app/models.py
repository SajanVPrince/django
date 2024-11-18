from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.TextField()
    email=models.EmailField()
    dob=models.DateField()
    phone=models.IntegerField()
    