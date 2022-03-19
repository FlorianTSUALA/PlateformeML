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
    logout(request)
    return redirect('dashbord')

#def register(request):
 #   form = CreateUser()
  #  if request.method == 'POST':
   #     form = CreateUser(request.POST)
    #    if form.is_valid():
     #       form.save()
      #      user=form.cleaned_data.get('username')
       #     messages.success(request, 'Votre compte a été creer.' + user)
        #    return redirect('login')
        #else:
         #   print('invalide data')
        #form = CreateUser()

    #context = {'form': form}
    #return render(request, 'register.html',context)

# def register(request):
#     form = CreateUser()
#     if request.method == 'POST':
#         user = User()
#         form = CreateUser(request.POST)
#         username = request.POST.get('username')
#         print(form)
#         if form.is_valid():
#             form.save()
#             user=form.cleaned_data.get('username')
#             messages.success(request, 'Votre compte a été creer.' + user)
#             return redirect('login')
#             print('ok')
#         else:
#             print('invalide data')
#            # form = CreateUser()

#     context = {'form': form}
#     return render(request, 'register.html',context)


# def register(request):
#     if request.method == "POST":
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             pwd = form.cleaned_data['pwd']
#             user = User.objects.create_user(username= username, password= pwd)
#             if user is not None:
#                 return redirect('login_login')
#             else:
#                 messages.error(request, 'creation de compte échouée')
#                 render(request,'users/register.html',{'form':form})
#         else:
#             return render(request, 'users/register.html',{'form':form})
#     return render(request,'users/register.html',{'form':form}) 




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