from django.urls import path
from . import views

urlpatterns = [
    path('demo',views.demo),
    path('dem/<int:a>',views.demo1),
    path('q1/<int:a>/<int:b>',views.q1),
    path('q2/<a>',views.q2),
    path('q3/<int:a>',views.q3),
    path('q4/<int:a>',views.q4),
    path('q5/<int:a>',views.q5),
    path('q6/<int:a>',views.q6),
    path('demo',views.dem),
    path('disp',views.disp),
    path('add',views.add),
    path('edit_usr/<id>',views.edit_usr),
    path('dlt_usr/<id>',views.dlt_usr),
    path('',views.index),
    path('dispstd',views.disp_std),
    path('addstd',views.add_std),
    path('editstd/<id>',views.edt_std),
    path('dltstd/<id>',views.dlt_std),
]
