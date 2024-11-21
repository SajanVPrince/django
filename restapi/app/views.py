from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializer import *
# Create your views here.
def user_ser(req):
    if req.method=='GET':
        data=student.objects.all()
        d=user_seri(data,many=True)
        return JsonResponse(d.data,safe=False)