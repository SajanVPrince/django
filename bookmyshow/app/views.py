from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(req):
    data=Movies.objects.all()
    return render(req,'index.html',{'data':data})

def movie_details(req,mid):
    data1=Movies.objects.get(pk=mid)
    return render(req,'sec.html',{'data1':data1})