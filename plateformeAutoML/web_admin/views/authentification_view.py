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
            return render(request, 'users/login.html')
    else:
        return render(request, 'users/login.html')
    return render(request,'users/login.html')