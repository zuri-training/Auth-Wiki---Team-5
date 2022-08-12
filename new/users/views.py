# users/views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class Password_ChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'password_change.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('users:login')
'''
from django.http import HttpResponse
from django.urls import reverse_lazy


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm, CustomUserChangeForm

'''
