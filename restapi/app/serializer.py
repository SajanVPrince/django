from rest_framework import serializers

class user_seri(serializers.Serializer):
    roll=serializers.IntegerField()
    name=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.EmailField()


