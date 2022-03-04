from django.shortcuts import render
from django.urls import reverse_lazy
from web_admin.models import Algorithme
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import JsonResponse

class AccueilView(TemplateView):
    template_name = 'accueil.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['users'] = Algorithme.objects.all()
    #     return context
