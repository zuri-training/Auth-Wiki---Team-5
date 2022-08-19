# Authwiki/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Authwiki, Enquiry
from django.views.generic.edit import CreateView
#from django.views.generic.edit import UpdateView 
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin



class AuthwikiListView(ListView):
    model = Authwiki
    template_name = 'library.html'

class AuthwikiDetailView(LoginRequiredMixin, DetailView): # new
    model = Authwiki
    template_name = 'authwiki_detail.html'
    context_object_name = 'indiv_post'
    login_url = 'login'

# class AuthwikiUpdateView(LoginRequiredMixin, UpdateView): # new
#     model = Authwiki
#     fields = ('name', 'description', )
#     template_name = 'authwiki_edit.html'
#     login_url = 'login'

'''
def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
'''
# class AuthwikiDeleteView(LoginRequiredMixin, DeleteView): # new
#     model = Authwiki
#     template_name = 'authwiki_delete.html'
#     success_url = reverse_lazy('library')
#     login_url = 'login'

#     def dispatch(self, request, *args, **kwargs): # new
#             obj = self.get_object()
#             if obj.author != self.request.user:
#                 raise PermissionDenied
#             return super().dispatch(request, *args, **kwargs)

class AuthwikiCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Authwiki
    template_name = 'authwiki_new.html'
    fields = ('name', 'description','cover' )
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)

'''
def authwiki(request, pk):
    authwikis = Authwiki.objects.get(id=pk)
    return render (request, 'authwiki_detail.html', {'authwikis':authwikis})
'''


def search_results(request):
    if request.method=="POST":
        searched = request.POST['searched']
        results = Authwiki.objects.filter(name__contains=searched)
        return render (request, 'search_results.html', {'searched':searched, 'results':results})
    else:
        return render (request, 'search_results.html', {})

def Contact(request):
    #print (request.POST)
    if request.method == "POST":
        email = request.POST.get("email")
        content = request.POST.get("content")
        #print(email, content)
        Enquiry.objects.create(email=email, content=content)
    return render (request, 'contact.html', {})

def Contact0(request):
    if request.method == "POST":
        email = request.POST.get("email")
        content = request.POST.get("content")
        Enquiry.objects.create(email=email, content=content)
    return render (request, 'unauthcontact.html', {})

def Documentation(request):
    return render (request, 'Documentation.html', {})

def Documentation0(request):
    return render (request, 'unauth_Documentation.html', {})  



