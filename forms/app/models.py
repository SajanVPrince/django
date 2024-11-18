from django.db import models

# Create your models here.
class Students(models.Model):
    roll=models.IntegerField()
    name=models.TextField()
    age=models.IntegerField()
    email=models.EmailField()