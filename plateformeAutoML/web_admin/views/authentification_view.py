import email
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from web_admin.models import Algorithme
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def login(request):
    return render(request, 'pages/authentification/login.html')


def registers(request):
    return render(request, 'pages/authentification/register.html')

def connexion(request):
    if request.method == "POST":
        username = request.POST['login']
        pwd = request.POST['password']
        print('le nom est :',username)
        user = authenticate(username=username,password= pwd)
        if user is not None:
            print("utilisateur existant")
            return redirect('vitrine')
        else:
            messages.error(request, "erreur t'authentification")
            return render(request, 'pages/authentification/login.html')
    else:
        return render(request, 'pages/authentification/login.html')
    return render(request,'pages/authentification/login.html')


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
    if not request.user.is_authenticated:
        logout(request)
    return redirect(settings.LOGIN_URL)


def register(request):
    if request.method == "POST":
        username = request.POST.get('login')
        email = request.POST.get('email')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')
        if pwd1 == pwd2:
            user = User.objects.create_user(username= username, email = email, password= pwd1)
            return redirect('login')
        # if user is not None:
        #     return redirect('login_login')
        else:
            messages.error(request, 'creation de compte échouée')
            render(request,'pages/authentification/register.html')
    else:
        return render(request, 'pages/authentification/register.html')
    return render(request,'pages/authentification/register.html') 



def liste_user(request):
    utilisateur = User.objects.all()
    return render(request,'pages/authentification/liste_user.html')

def register(request):
    print('registration')
    if request.method == "POST":
        username = request.POST.get('username')
        nom = request.POST.get('nom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        pwd1 = request.POST.get('passw1')
        pwd2 = request.POST.get('passw2')
        if pwd1 !=pwd2:
            message = 'Les mots de passes ne sont pas identique'
            return render(request,'auth/auth_register.html',{'message':message})
        else:
           dk = hashlib.pbkdf2_hmac('sha256', str.encode(pwd1), b'salt', 10000)
           password = binascii.hexlify(dk)
           compte = Compte(
                            email = email,
                            name = nom,
                            username = username,
                            telephone = telephone,
                            password = password
                        )
           compte.save()
           return redirect(settings.LOGIN_URL)

            # messages.error(request, 'creation de compte échouée')
            # render(request,'users/register.html',{'form':form})
    else:
        return render(request, 'auth/auth_register.html')
        
    return render(request,'auth/auth_register.html')

def user_login(request):
    redirect_to = request.POST.get(REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME, reverse('gestionnaire')))

    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to)

    if request.method == "POST":
        
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        try:
            utilisateur = Compte.objects.get(username=username)
        except ObjectDoesNotExist:
            message = 'Votre identifiant ou votre mot de passe est incorrect'
            return render(request,'auth/auth_login.html',{'message':message})
        
        dk = hashlib.pbkdf2_hmac('sha256', str.encode(pwd), b'salt', 10000)
        password = binascii.hexlify(dk)

        print("User Active State : ", utilisateur.is_active)

        if str(password) == str(utilisateur.password):
            if  utilisateur.is_active:
                # The default Django's "remember me" lifetime is 2 weeks and can be changed by modifying
                # the SESSION_COOKIE_AGE settings' option.
                if settings.USE_REMEMBER_ME:
                    if not remember_me:
                        request.session.set_expiry(0)
                login(request, utilisateur)
                return redirect(redirect_to)
            else:
                pass
        else:
            message = 'Votre identifiant ou votre mot de passe est incorrect'
            return render(request,'auth/auth_login.html',{'message':message})
    else:
        return render(request, 'auth/auth_login.html')