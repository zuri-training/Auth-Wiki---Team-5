from django.urls import path
from Authwiki import views

urlpatterns = [
    path('', views.home, name='home'),
]