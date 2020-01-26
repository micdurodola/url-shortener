from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import short_urls
from .forms import UrlForm
from main.shortener import shortener


# Create your views here.

def make(request):
    form = UrlForm(request.POST)
    a =""
    if request.method =="POST":
        if form.is_valid():
            NewUrl = form.save(commit =False)
            a = shortener().issue_token()
            NewUrl.short_url = a
            NewUrl.save()
        
        else:
            form = UrlForm()
            a="Invalid URL"
    return render (request, 'home.html',{'form':form,'a':a})

def Home(request, token):
    long_url = short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)

        
