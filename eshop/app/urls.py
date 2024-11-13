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
    path('booking',views.booking),



#-------------------User----------------------

    path('register',views.register),
    path('user_home',views.user_home),
    path('view_prod/<pid>',views.view_prod),
    path('add_to_cart/<pid>',views.add_to_cart),
    path('view_cart',views.view_cart),
    path('dlt_cart/<id>',views.delete_cart),
    path('cart_buy/<cid>',views.cart_buy),
    path('user_buy/<pid>',views.usr_buy),
    path('usr_booking',views.usr_booking),

]