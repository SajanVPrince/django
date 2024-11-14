from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')

def movie_details(req):
    return render(req,'sec.html')