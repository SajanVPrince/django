from django.urls import path
from . import views

urlpatterns = [
    path('',views.shp_login),
    path('shp_logout',views.shp_logout),

#------------------Shop------------------

    path('shp_home',views.shp_home),


]