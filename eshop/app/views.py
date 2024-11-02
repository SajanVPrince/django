from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *

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
            return render(req,'login1.html')
    
    else:
        return render(req,'login.html')

def shp_home(req):
    if 'eshop' in req.session:
        return render(req,'shop/home.html')
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