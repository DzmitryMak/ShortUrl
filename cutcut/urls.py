from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('/create', views.create, name='create'),
    path('<str:pk>', views.redir, name='go'),
    path('/list_urls', views.list_url, name='list_urls'),

]

