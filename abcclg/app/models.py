from django.db import models

# Create your models here.
class abcclg(models.Model):
    name=models.TextField()
    about=models.TextField()
    mission=models.TextField()
    vision=models.TextField()
    phone=models.IntegerField()
    email=models.EmailField()
    course=models.TextField()
    feature=models.TextField()

class cntct(models.Model):
    name=models.TextField()
    phone=models.IntegerField()
    sub=models.TextField()
    message=models.TextField()
    email=models.EmailField()

    
