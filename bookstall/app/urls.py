from django.urls import path
from . import views

urlpatterns = [
    path('',views.bk_login),

    # --------------seller------------------

    path('sellerhome',views.seller_home),


]