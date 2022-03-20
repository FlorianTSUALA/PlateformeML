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



def login(request):
    return render(request, 'pages/authentification/login.html')


def registers(request):
    return render(request, 'pages/authentification/register.html')

def connexion(request):
    redirect_to = request.POST.get(REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME, reverse('home')))
    print(redirect_to)
    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to)

    if request.method == "POST":
        
        login = request.POST.get('login')
        password = request.POST.get('pwd')
        remember_me = request.POST.get('remember_me')

        try:
            compte = Compte.objects.get(login=login)
        except ObjectDoesNotExist:
            message = 'Votre identifiant ou votre mot de passe est incorrect'
            return render(request,'pages/authentification/login.html',{'message':message})
        
        dk = hashlib.pbkdf2_hmac('sha256', str.encode(password), b'salt', 10000)
        password = binascii.hexlify(dk)

        print("User Active State : ", compte.is_active)
        print(str(password) ,"  ", str(compte.password))
        if str(password) == str(compte.password):
            if  compte.is_active:
                # The default Django's "remember me" lifetime is 2 weeks and can be changed by modifying
                # the SESSION_COOKIE_AGE settings' option.
                if settings.USE_REMEMBER_ME:
                    if not remember_me:
                        request.session.set_expiry(0)
                auth_login(request, compte)
                return redirect(redirect_to)
            else:
                pass
        else:
            message = 'Votre identifiant ou votre mot de passe est incorrect'
            return render(request,'pages/authentification/login.html',{'message':message})
    else:
        return render(request, 'pages/authentification/login.html')

def loginPage(request):
    if request.method == 'POST':
        login=request.POST.get('login')
        password=request.POST.get('password') 
        print(login)
        print(password)
        
        user = authenticate(request,login=login,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or password is not correct')    
    return render(request, 'login.html')

def logoutUser(request):
    if not request.user.is_authenticated:
        logout(request)
    return redirect(settings.LOGIN_URL)


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
                            compte = compte
                        )
           utilisateur.save()

           return redirect(settings.LOGIN_URL)

            # messages.error(request, 'creation de compte échouée')
            # render(request,'users/register.html',{'form':form})
    else:
        return render(request, 'pages/authentification/register.html')
        
    return render(request,'pages/authentification/register.html')

