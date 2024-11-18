from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import *
from .models import *

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
            messages.warning(req,"please check your username or password")
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
            messages.warning(req,"email already exists enter a new email id")
            return render(req,'register.html')
    else:
        return render(req,'register.html')

def user_home(req):
    if 'user' in req.session:
        data=Img.objects.all()
        data1=Vdo.objects.all()
        return render(req,'user/home.html',{'data':data,'data1':data1})
    else:
        return redirect(m_login)
      

def img_upd(req):
    if 'user' in req.session:
        if req.method=='POST':
            img=req.FILES['img']
            user=User.objects.get(username=req.session['user'])
            data=Img.objects.create(img=img,user=user)
            data.save()
            return redirect(user_home)
        else:
            return render(req,'user/image.html')
    else:
        return redirect(m_login)
    
def vid_upd(req):
    if 'user' in req.session:
        if req.method=='POST':
            vid=req.FILES['vid']
            user=User.objects.get(username=req.session['user'])
            data=Vdo.objects.create(vid=vid,user=user)
            data.save()
            return redirect(user_home)
        else:
            return render(req,'user/video.html')
    else:
        return redirect(m_login)