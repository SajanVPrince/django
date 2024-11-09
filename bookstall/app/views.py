from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import *
from django.contrib import messages
from .models import *
import os


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
    
def main_logout(req):
    req.session.flush()          #delete session
    logout(req)
    return redirect(bk_login)

def seller_home(req):
    if 'book' in req.session:
        data=Books.objects.all()
        return render(req,'seller/home.html',{'book':data})
    else:
        return redirect(bk_login)

def add_bk(req):
    if 'book' in req.session:
        if req.method=='POST':
            bk_id=req.POST['bk_id']
            bk_name=req.POST['bk_name']
            ath_name=req.POST['ath_name']
            bk_price=req.POST['bk_price']
            bk_genres=req.POST['bk_genres']
            ofr_price=req.POST['ofr_price']
            img=req.FILES['img']
            bk_dis=req.POST['bk_dis']
            data=Books.objects.create(bk_id=bk_id,name=bk_name,ath_name=ath_name,price=bk_price,bk_genres=bk_genres,ofr_price=ofr_price,img=img,dis=bk_dis)
            data.save()
            return redirect(add_bk)
        else:
            return render(req,'seller/addbook.html')
    else:
        return redirect(bk_login)

def edit_bk(req,pid):
    if 'book' in req.session:
        if req.method=='POST':
            bk_id=req.POST['bk_id']
            bk_name=req.POST['bk_name']
            ath_name=req.POST['ath_name']
            bk_price=req.POST['bk_price']
            bk_genres=req.POST['bk_genres']
            ofr_price=req.POST['ofr_price']
            img=req.FILES.get('img')
            bk_dis=req.POST['bk_dis']
            if img:
                Books.objects.filter(pk=pid).update(bk_id=bk_id,name=bk_name,ath_name=ath_name,price=bk_price,bk_genres=bk_genres,ofr_price=ofr_price,img=img,dis=bk_dis)
                data=Books.objects.get(pk=pid)
                data.img=img
                data.save()
            else:
                Books.objects.filter(pk=pid).update(bk_id=bk_id,name=bk_name,ath_name=ath_name,price=bk_price,bk_genres=bk_genres,ofr_price=ofr_price,dis=bk_dis)
            return redirect(seller_home)
        else:
            data=Books.objects.get(pk=pid)
            return render(req,'seller/edit.html',{'product':data})
    else:
        return redirect(bk_login) 

def dlt_bk(req,pid):
    data=Books.objects.get(pk=pid)
    url=data.img.url
    og_path=url.split('/')[-1]
    os.remove('media/'+og_path)
    data.delete()
    return redirect(seller_home)   

# def ddlink(req):
#     if 'book' in req.session:
#         data=Books.objects.all()
#         if dd=bk_genres:
#             return render(req,'seller/home.html',{'book':data})
#     else:
#         return redirect(bk_login)    