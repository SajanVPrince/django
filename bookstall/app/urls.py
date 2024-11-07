from django.urls import path
from . import views

urlpatterns = [
    path('',views.bk_login),
    path('main_logout',views.main_logout),


    # --------------seller------------------

    path('sellerhome',views.seller_home),
    path('add_bk',views.add_bk),



]