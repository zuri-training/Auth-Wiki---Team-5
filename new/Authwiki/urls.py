# articles/urls.py
from django.urls import path
from .views import AuthwikiListView
urlpatterns = [
path('', AuthwikiListView.as_view(), name='article_list'),
]
