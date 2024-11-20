from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.TextField()
    date=models.DateField()
    img=models.FileField()
    backimg=models.FileField()
    dim=models.TextField()
    lang=models.TextField()
    duration=models.TextField()
    certi=models.TextField()
    about=models.TextField()
    genres=models.TextField()