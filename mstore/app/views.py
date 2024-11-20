from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import *
from .models import *
import os

# Create your views here.
def m_login(req):
    if 'mshop' in req.session:
        return redirect(m_home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['mshop']=uname   #create session
                return redirect(m_home)
            else:
                login(req,data)
                req.session['user']=uname
                return redirect(user_home)
        else:
            return render(req,'login.html')
    
    else:
        return render(req,'login.html')

def m_logout(req):
    req.session.flush()          #delete session
    logout(req)
    return redirect(m_login)


def m_home(req):
    return render(req,'admin/home.html')

# -------------------------USER---------------------

def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
            data.save()
            return redirect(m_login)
        except:
            return render(req,'register.html')
    else:
        return render(req,'register.html')

def user_home(req):
    if 'user' in req.session:
        user=User.objects.get(username=req.session['user'])
        data=Img.objects.filter(user=user)
        data1=Vdo.objects.filter(user=user)
        return render(req,'user/home.html',{'data':data,'data1':data1})
    else:
        return redirect(m_login)
      

def file_upd(req):
    if 'user' in req.session:
        if req.method=='POST':
            file=req.FILES['file']
            nm_img=file.name
            ex_img=nm_img.split('.')[-1]
            print(ex_img)
            if ex_img in ['jpg','jpeg']:
                user=User.objects.get(username=req.session['user'])
                data=Img.objects.create(img=file,user=user)
                data.save()
                return redirect(user_home)
            elif ex_img in['mp4']:
                user=User.objects.get(username=req.session['user'])
                data=Vdo.objects.create(vid=file,user=user)
                data.save()
                return redirect(user_home)
            else:
                return redirect(user_home)
        else:
            return render(req,'user/file.html')
    else:
        return redirect(m_login)
    
def dlt_img(req,fid):
    data=Img.objects.get(pk=fid)
    data1=Vdo.objects.get(pk=fid)
    url=data.img.url
    url1=data1.vid.url
    og_path=url.split('/')[-1]
    og_path1=url1.split('/')[-1]
    os.remove('media/'+og_path)
    os.remove('media/'+og_path1)
    data.delete()
    data1.delete()
    return redirect(user_home)
