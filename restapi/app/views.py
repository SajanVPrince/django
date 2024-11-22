from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .serializer import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
def user_ser(req):
    if req.method=='GET':
        data=student.objects.all()
        d=user_seri(data,many=True)
        return JsonResponse(d.data,safe=False)

@csrf_exempt   
def model_serializer(req):
    if req.method=='GET':
        data=student.objects.all()
        d=model_ser(data,many=True)
        return JsonResponse(d.data,safe=False)
    elif req.method=='POST':
        d=JSONParser().parse(req)
        data=model_ser(data=d)
        if data.is_valid():
            data.save()
            return JsonResponse(data.data)
        else:
            return JsonResponse(data.errors)


