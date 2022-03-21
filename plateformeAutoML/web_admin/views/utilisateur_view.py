from django.shortcuts import render
from django.urls import reverse_lazy
from web_admin.models import Algorithme
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import JsonResponse

#######

import email
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth import (authenticate, login, logout, get_user_model, REDIRECT_FIELD_NAME)
from django.core.exceptions import ObjectDoesNotExist
import hashlib, binascii
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from web_admin.models import Compte, Utilisateur
from django.conf import settings

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


def register(request):
    print('registration')
    if request.method == "POST":
        login = request.POST.get('login')
        email = request.POST.get('email')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
        
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        pays = request.POST.get('pays')
        ville = request.POST.get('ville')
        description = request.POST.get('description')

        if pwd1 !=pwd2:
            message = 'Les mots de passes ne sont pas identiques'
            return render(request,'pages/authentification/register.html',{'message':message})
        else:
           dk = hashlib.pbkdf2_hmac('sha256', str.encode(pwd1), b'salt', 10000)
           password = binascii.hexlify(dk)
           compte = Compte(
                            login = login,
                            email = email,
                            password = password
                        )
           compte.save()

           utilisateur = Utilisateur(
                            nom = nom,
                            prenom = prenom,
                            telephone = telephone,
                            pays = pays,
                            compte = compte,
                            description = description,
                            ville = ville
                        )
           utilisateur.save()

           return redirect(settings.LOGIN_URL)

            # messages.error(request, 'creation de compte échouée')
            # render(request,'users/register.html',{'form':form})
    else:
        return render(request, 'pages/utilisateur/create_utilisateur.html')
        
    return render(request,'pages/utilisateur/create_utilisateur.html')





class ListUtilisateurView(TemplateView):
    template_name = 'pages/utilisateurs/list_utilisateur.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_title'] = 'Utilisateurs'
        context['section_item_title'] = 'Liste des utilisateurs'
        return context



def loginPage(request):
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

def logoutUser(request):
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

