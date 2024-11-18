from django.urls import path
from . import views

urlpatterns = [
    path('',views.usr_form),
]
