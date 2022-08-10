from ast import Return
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(response):
    return HttpResponse('<h1>Home Page</h1>')
