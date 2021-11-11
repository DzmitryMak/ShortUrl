import base64
from django.shortcuts import render, redirect, HttpResponse
from . models import Url
from .forms import UrlForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'base.html')


@login_required
def create(request):
    """Create new model URL. Attribute short is obtained by encoding base64
    If URL.long already in db, just return short URL.short, and add new author"""
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            long = request.POST['long']
            if Url.objects.filter(long=long).exists():
                already_in_db = Url.objects.get(long=long)
                request.user.url_set.add(already_in_db)
                data = {'short': 'http://127.0.0.1:8000/' + already_in_db.short, 'form': form}
                return render(request, 'cutcut/shortener.html', data)
            short = str(base64.b64encode(long.encode()))[-7:-1]
            new_url = form.save(commit=False)
            new_url.short = short
            new_url.save()
            new_url.author.add(request.user)
            data = {'short': 'http://127.0.0.1:8000/' + short, 'form': form}
            return render(request, 'cutcut/shortener.html', data)
        else:
            return HttpResponse('форма заполнена неверно')
    else:
        form = UrlForm()
    return render(request, 'cutcut/shortener.html', {'form': form})


def redir(request, pk):
    """func just redirect to original url """
    new = Url.objects.get(short=pk)
    return redirect(new.long)


def list_url(request):
    """show all URLs of authorized author"""
    if request.user.is_authenticated:
        urls = request.user.url_set.all()
    else:
        return redirect('login')
    return render(request, 'cutcut/list_url.html', {'urls': urls})
