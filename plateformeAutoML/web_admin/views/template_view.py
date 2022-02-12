from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

def create_project(request):
    return render(request, 'includes/profile-list.html',{profiles: profiles})

def use_projet(request):
    return render(request, 'includes/profile-list.html',{profiles: profiles})

def manage_parametrage(request):
    return render(request, 'includes/profile-list.html',{profiles: profiles})

def download_res_project(request):
    return render(request, 'includes/profile-list.html',{profiles: profiles})

def entity_project(request):
    return render(request, 'includes/profile-list.html',{profiles: profiles})