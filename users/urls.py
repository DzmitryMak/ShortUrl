from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('complete', views.complete, name='complete'),

]
