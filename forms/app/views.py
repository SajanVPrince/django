from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def usr_form(req):
    if req.method=='POST':
        form1=user_form(req.POST)
        if form1.is_valid():
            roll=form1.cleaned_data['roll_num']
            name=form1.cleaned_data['name']
            age=form1.cleaned_data['age']
            email=form1.cleaned_data['email']
            data=Students.objects.create(roll=roll,name=name,age=age,email=email)
            data.save()
            return redirect(usr_form)
    form=user_form()
    return render(req,'form1.html',{'form':form})

def modelform(req):
    if req.method=='POST':
        form1=model_form(req.POST)
        if form1.is_valid():
            form1.save()
        return redirect(modelform)
    else:
        form=model_form()
        return render(req,'model.html',{'form':form})