from django.urls import path
from . import views

urlpatterns = [
    path('',views.m_login),
    path('register',views.register),
    path('m_home',views.m_home),
    path('m_logout',views.m_logout),




# ------------user---------

    path('user_home',views.user_home),
    path('img_upd',views.img_upd),
    path('vid_upd',views.vid_upd),




]
