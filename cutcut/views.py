import base64
from django.shortcuts import render, redirect, HttpResponse
from . models import Url
from .forms import UrlForm


def home(request):
    return render(request, 'base.html')


def create(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            long = request.POST['long']
            if Url.objects.filter(long=long).exists():
                already_in_db = Url.objects.get(long=long)
                data = {'short': 'http://127.0.0.1:8000/' + already_in_db.short, 'form': form}
                return render(request, 'cutcut/shortener.html', data)
            short = str(base64.b64encode(long.encode()))[-7:-1]
            new_url = form.save(commit=False)
            new_url.short = short
            new_url.author = request.user
            new_url.save()
            data = {'short': 'http://127.0.0.1:8000/' + short, 'form': form}
            return render(request, 'cutcut/shortener.html', data)
        else:
            return HttpResponse('форма заполнена неверно')
    else:
        form = UrlForm()
    return render(request, 'cutcut/shortener.html', {'form': form})


def redir(request, pk):
    new = Url.objects.get(short=pk)
    return redirect(new.long)


def list_url(request):
    if request.user.is_authenticated:
        username = request.user.username
        urls = Url.objects.all().filter(author__username=username)
    else:
        return redirect('login')
    return render(request, 'cutcut/list_url.html', {'urls': urls, 'username': username})
