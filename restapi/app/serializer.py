from rest_framework import serializers
from .models import *

class user_seri(serializers.Serializer):
    roll=serializers.IntegerField()
    name=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.EmailField()

class model_ser(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'


