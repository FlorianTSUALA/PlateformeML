from django.shortcuts import render
from django.urls import reverse_lazy
from web_admin.models import Algorithme
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import JsonResponse

class MonCompteView(TemplateView):
    template_name = 'pages/utilisateurs/mon_compte.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_white_text'] = True
        context['section_title'] = 'Utilisateur'
        context['section_item_title'] = 'Mon Compte'
        return context


class CreateUtilisateurView(TemplateView):
    template_name = 'pages/utilisateurs/create_utilisateur.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_white_text'] = True
        context['section_title'] = 'Utilisateur'
        context['section_item_title'] = 'Mon Compte'
        return context


class ListUtilisateurView(TemplateView):
    template_name = 'pages/utilisateurs/list_utilisateur.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_title'] = 'Utilisateurs'
        context['section_item_title'] = 'Liste des utilisateurs'
        return context



def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password') 
        print(username)
        print(password)
        
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or password is not correct')    
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('dashbord')


def register(request):
    form = CreateUser()
    if request.method == 'POST':
        user = User()
        form = CreateUser(request.POST)
        username = request.POST.get('username')
        print(form)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Votre compte a été creer.' + user)
            return redirect('login')
            print('ok')
        else:
            print('invalide data')
           # form = CreateUser()

    context = {'form': form}
    return render(request, 'register.html',context)

