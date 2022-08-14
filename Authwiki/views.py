from django.shortcuts import render
# Authwiki/views.py
from django.views.generic import ListView
from .models import Authwiki



class AuthwikiListView(ListView):
    model = Authwiki
    template_name = 'library.html'


def Contact(request):
    return render (request, 'contact.html', {})

def Contact0(request):
    return render (request, 'unauthcontact.html', {})

def Documentation(request):
    return render (request, 'Documentation.html', {})

def Documentation0(request):
    return render (request, 'unauth_Documentation.html', {})    

