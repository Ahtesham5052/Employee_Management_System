from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage) ,
    path('all_emp', views.all_emp) ,
    path('add_emp', views.add_emp) ,
    path('remove_emp', views.remove_emp),
    path('filter_emp', views.filter_emp) ,
]
