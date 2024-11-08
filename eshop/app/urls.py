from django.urls import path
from . import views

urlpatterns = [
    path('',views.shp_login),
    path('shp_logout',views.shp_logout),

#------------------Shop------------------

    path('shp_home',views.shp_home),
    path('add_prod',views.add_prod),
    path('edit_prod/<pid>',views.edit_prod),
    path('dlt_prd/<pid>',views.dlt_prd),


#-------------------User----------------------

    path('register',views.register),
    path('user_home',views.user_home),
    path('view_prod/<pid>',views.view_prod),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('view_cart',views.view_cart),



]