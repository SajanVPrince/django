from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(req):
    data=Phone.objects.all().order_by('name')
    return render(req,'home.html',{'data':data})

def add(req):
    if req.method=='POST':
        name=req.POST['name'].capitalize()
        email=req.POST['email'].lower()
        place=req.POST['place']
        phone=req.POST['phone']
        phone_num=f"+91_{phone}"
        whatsapp=req.POST['whatsapp']
        if whatsapp:
            whatsapp_link=f"https://wa.me/{whatsapp}"
        else:
            whatsapp_link='unavailable'
        data=Phone.objects.create(name=name,email=email,place=place,phone=phone_num,whatsapp=whatsapp_link)
        data.save()
        return redirect(home)
    else:
        return render(req,'add.html')