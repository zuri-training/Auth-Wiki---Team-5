# articles/urls.py
from django.urls import path
from .views import AuthwikiListView, Contact, Documentation, Documentation0, Contact0
urlpatterns = [
path('', AuthwikiListView.as_view(), name='library'),
path('contact-us/', Contact, name='contact'),
path('documentation/', Documentation, name='documentation'),
path('documentation/', Documentation0, name='documentation0'),
path('contact-us/', Contact0, name='contact0'),
]
