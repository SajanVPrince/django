from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import *
from django.contrib import messages


# Create your views here.

def bk_login(req):
    if 'book' in req.session:
        return redirect(seller_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            req.session['book']=uname   #create session
            return redirect(seller_home)
        else:
            messages.warning(req,"please check your username or password")
            return render(req,'login.html')
    
    else:
        return render(req,'login.html')

def seller_home(req):
    return render(req,'seller/home.html')