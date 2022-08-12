from django.shortcuts import render
# Authwiki/views.py
from django.views.generic import ListView
from .models import Authwiki



class AuthwikiListView(ListView):
    model = Authwiki
    template_name = 'library.html'


