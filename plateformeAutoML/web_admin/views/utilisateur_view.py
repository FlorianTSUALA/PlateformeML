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


