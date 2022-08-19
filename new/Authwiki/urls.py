# articles/urls.py
from django.urls import path
from .views import AuthwikiListView, Contact, Documentation, Documentation0, Contact0, search_results
from .views import (AuthwikiListView, AuthwikiListView, AuthwikiDetailView, AuthwikiCreateView)

urlpatterns = [
path('', AuthwikiListView.as_view(), name='library'),
path('contact-us/', Contact, name='contact'),
path('documentation/', Documentation, name='documentation'),
path('documentation/', Documentation0, name='documentation0'),
path('contact-us/', Contact0, name='contact0'),
path('search_results/', search_results, name='search-results'),
path('<int:pk>/detail/', AuthwikiDetailView.as_view(), name='authwiki_detail'), 
#path('<int:pk>/delete/', AuthwikiDeleteView.as_view(), name='authwiki_delete'), # new
path('new/', AuthwikiCreateView.as_view(), name='authwiki_new'),
]
