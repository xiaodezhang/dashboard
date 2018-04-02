from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin_page,name = 'signin_page'),
    path('signin', views.signin),
    path('index', views.index,name = 'index'),
    path('order', views.order),
    path('reporter', views.reporter),
    path('employee_management', views.employee_management),
    path('settings', views.settings),
    path('res', views.res),
    path('marketing', views.marketing),
]
