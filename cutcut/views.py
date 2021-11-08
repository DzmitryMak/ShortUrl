from django.shortcuts import render, redirect, HttpResponse
from .forms import UrlForm
from . import forms
from django.views.generic.edit import FormView
from . models import Url
from django.urls import reverse_lazy
import base64
from django.contrib.auth.models import User
from . import models

def home(request):
    return render(request, 'base.html')


def create(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            long = request.POST['long']
            short = str(base64.b64encode(long.encode()))[-7:-1]
            new_url = form.save(commit=False)
            new_url.short = short
            new_url.author = request.user
            new_url.save()
            return HttpResponse('http://127.0.0.1:8000/' + short)
        else:
            return HttpResponse('форма заполнена неверно')
    else:
        form = UrlForm()
    return render(request, 'cutcut/shortener.html', {'form': form})


def redir(request, pk):
    new = Url.objects.get(short=pk)
    return redirect(new.long)


def list_url(request):
    urls = Url.objects.all()
    user = User
    return render(request, 'cutcut/list_url.html', {'urls': urls, 'user': user})

