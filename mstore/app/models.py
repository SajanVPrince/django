from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Img(models.Model):
    img=models.FileField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Vdo(models.Model):
    vid=models.FileField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
