from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(req):
    data=abcclg.objects.all()
    for i in data:
        a=i.course.split(',')
        b=i.feature.split(',')
    return render(req,'home.html',{'data':data,'a':a,'b':b})

def h1(req):
    home()

def contact(req):
    data=abcclg.objects.all()
    for i in data:
        a=i.course.split(',')
    if req.method=='POST':
            name=req.POST['name']
            phone=req.POST['phone']
            email=req.POST['email']
            subject=req.POST['subject']
            message=req.POST['message']
            data=cntct.objects.create(name=name,phone=phone,email=email,sub=subject,message=message)
            data.save()
            return redirect(contact)
    return render(req,'contact.html',{'data':data,'a':a})

def about(req):
    data=abcclg.objects.all()
    for i in data:
        a=i.course.split(',')
        b=i.feature.split(',')
    return render(req,'about.html',{'data':data,'a':a,'b':b})