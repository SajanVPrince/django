from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import *
from django.contrib import messages
from .models import *
import os

def shp_login(req):
    if 'eshop' in req.session:
        return redirect(shp_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pswd']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            req.session['eshop']=uname   #create session
            return redirect(shp_home)
        else:
            messages.warning(req,"please check your username or password")
            return render(req,'login.html')
    
    else:
        return render(req,'login.html')

def shp_home(req):
    if 'eshop' in req.session:
        data=Product.objects.all()  #can use slicing here
        return render(req,'shop/home.html',{'products':data})
    else:
        return redirect(shp_login)

def shp_logout(req):
    req.session.flush()          #delete session
    logout(req)
    return redirect(shp_login)

def add_prod(req):
    if 'eshop' in req.session:
        if req.method=='POST':
            prd_id=req.POST['prd_id']
            prd_name=req.POST['prd_name']
            prd_price=req.POST['prd_price']
            ofr_price=req.POST['ofr_price']
            img=req.FILES['img']
            prd_dis=req.POST['prd_dis']
            data=Product.objects.create(pro_id=prd_id,name=prd_name,price=prd_price,ofr_price=ofr_price,img=img,dis=prd_dis)
            data.save()
            return redirect(add_prod)
        else:
            return render(req,'shop/add_prod.html')
    else:
        return redirect(shp_login)
    
def edit_prod(req,pid):
    if 'eshop' in req.session:
        if req.method=='POST':
            prd_id=req.POST['prd_id']
            prd_name=req.POST['prd_name']
            prd_price=req.POST['prd_price']
            ofr_price=req.POST['ofr_price']
            prd_dis=req.POST['prd_dis']
            img=req.FILES.get('img')
            if img:
                Product.objects.filter(pk=pid).update(pro_id=prd_id,name=prd_name,price=prd_price,ofr_price=ofr_price,dis=prd_dis,img=img)
            else:
                Product.objects.filter(pk=pid).update(pro_id=prd_id,name=prd_name,price=prd_price,ofr_price=ofr_price,dis=prd_dis)
            return redirect(shp_home)
        else:
            data=Product.objects.get(pk=pid)
            return render(req,'shop/edit_prd.html',{'product':data})
    else:
        return redirect(shp_login)
    
def dlt_prd(req,pid):
    data=Product.objects.get(pk=pid)
    url=data.img.url
    og_path=url.split('/')[-1]
    os.remove('media/'+og_path)
    data.delete()
    return redirect(shp_home)

def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
            data.save()
            return redirect(shp_login)
        except:
            messages.warning(req,"email already exists enter a new email id")
            return render(req,'user/register.html')
    else:
        return render(req,'user/register.html')