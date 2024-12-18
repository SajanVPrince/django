from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
def usr_login(req):
    if 'pbook' in req.session:
        return redirect(home)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pswd']
        data=authenticate(username=uname,password=password)
        if data:
            if data.is_superuser:
                login(req,data)
                req.session['pbook']=uname   #create session
                # return redirect(home)
            else:
                login(req,data)
                req.session['user']=uname
                return redirect(home)
        else:
            messages.warning(req,"please check your username or password")
            return render(req,'login.html')
    
    else:
        return render(req,'login.html')

def usr_logout(req):
    req.session.flush()          #delete session
    logout(req)
    return redirect(usr_login)


def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
            data.save()
            return redirect(usr_login)
        except:
            messages.warning(req,"email already exists enter a new email id")
            return render(req,'register.html')
    else:
        return render(req,'register.html')

# def home(req):
#     if 'user' in req.session:
#         data=Phone.objects.all().order_by('name')
#         return render(req,'home.html',{'data':data})
#     else:
#         return redirect(usr_login)

def home(req):
    if 'user' in req.session:
        user = User.objects.get(username=req.session['user'])
        name=user.first_name
        data = Phone.objects.filter(user=user).order_by('name')
        return render(req, 'home.html', {'data': data,'name':name})
    else:
        return redirect('usr_login')


def add(req):
    if 'user' in req.session:
        if req.method=='POST':
            name=req.POST['name'].capitalize()
            email=req.POST['email'].lower()
            place=req.POST['place']
            phone=req.POST['phone']
            phone_num=f"+91_{phone}"
            whatsapp=req.POST['whatsapp']
            user=User.objects.get(username=req.session['user'])
            if whatsapp:
                whatsapp_link=f"https://wa.me/{whatsapp}"
            else:
                whatsapp_link='unavailable'
            data=Phone.objects.create(user=user,name=name,email=email,place=place,phone=phone_num,whatsapp=whatsapp_link)
            data.save()
            return redirect(home)
        else:
            return render(req,'add.html')
    else:
        return redirect(usr_login)