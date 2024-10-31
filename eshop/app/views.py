from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

def shp_login(req):
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['pswd']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)
            return redirect(shp_home)
        else:
            return render(req,'login1.html')
    
    else:
        return render(req,'login.html')

def shp_home(req):
    return render(req,'shop/home.html')

def shp_logout(req):
    logout(req)
    return redirect(shp_login)