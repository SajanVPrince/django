from django.urls import path
from . import views

urlpatterns = [
    path('',views.usr_form),
    path('model_form',views.modelform),

]
