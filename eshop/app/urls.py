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





]