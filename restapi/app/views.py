from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import *
from .serializer import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics,mixins
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


@csrf_exempt
def fun4(req,d):
    try:
        demo=student.objects.get(pk=d)
    except student.DoesNotExist:
        return HttpResponse('invalid')
    if req.method=='GET':
        s=model_ser(demo)
        return JsonResponse(s.data)
    elif req.method=='PUT':
        d=JSONParser().parse(req)
        s=model_ser(demo,data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
    elif req.method=='DELETE':
        demo.delete()
        return HttpResponse('deleted')
    
@api_view(['GET','POST'])
def fun5(req):
    if req.method=='GET':
        d=student.objects.all()
        s=model_ser(d,many=True)
        return Response(s.data)
    elif req.method=='POST':
        s=model_ser(data=req.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def fun6(req,d):
    try:
        demo=student.objects.get(pk=d)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method=='GET':
        s=model_ser(demo)
        return Response(s.data)
    elif req.method=='PUT':
        s=model_ser(demo,data=req.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif req.method=='DELETE':
        demo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class fun7(APIView):
    def get(self,req):
        demo=student.objects.all()
        s=model_ser(demo,many=True)
        return Response(s.data)
    def post(self,req):
        s=model_ser(data=req.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)
        
class fun8(APIView):
    def get(self,req,d):
        try:
            demo=student.objects.get(pk=d)
            s=model_ser(demo)
            return Response(s.data)
        except student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self,req,d):
        try:
            demo=student.objects.get(pk=d)
            s=model_ser(demo,data=req.data)
            if s.is_valid():
                s.save()
                return Response(s.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def delete(self,req,d):
        try:
            demo=student.objects.get(pk=d)
            demo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class genericapiview(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=model_ser
    queryset=student.objects.all()
    def get(self,req):
        return self.list(req)
    def post(self,req):
        return self.create(req)
    
class update(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class=model_ser
    queryset=student.objects.all()
    lookup_field='id'
    def get(self,req,id=None):
        return self.retrieve(req)
    def put(self,req,id=None):
        return self.update(req,id)
    def delete(self,req,id):
        return self.destroy(req,id)