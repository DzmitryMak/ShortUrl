from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('<str:pk>', views.redir, name='go'),
    path('/list_urls', views.list_url, name='list_urls'),

]
