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

def add_prod(req):
    if req.method=='POST':
        prd_id=req.POST['prd_id']
        prd_name=req.POST['prd_name']
        prd_price=req.POST['prd_price']
        ofr_price=req.POST['ofr_price']
        img=req.POST['img']
        prd_dis=req.POST['prd_dis']
        data=authenticate(pro_id=prd_id,name=prd_name,price=prd_price,ofr_price=ofr_price,img=img,dis=prd_dis)
        # data.save()
        return redirect(add_prod)
    else:
        return render(req,'shop/add_prod.html')