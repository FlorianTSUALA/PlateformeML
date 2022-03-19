from django.shortcuts import render
from django.urls import reverse_lazy
from web_admin.models import Algorithme
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import JsonResponse


class MesFavorisView(TemplateView):
    template_name = 'pages/projets/mes_favoris.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_white_text'] = False
        context['section_title'] = 'Mon espace'
        context['section_item_title'] = 'Mes favoris'
        return context


class MesProjetsView(TemplateView):
    template_name = 'pages/projets/mes_projets.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_white_text'] = False
        context['section_title'] = 'Mon espace'
        context['section_item_title'] = 'Mes Projets'
        return context


class ProjetsPublicsView(TemplateView):
    template_name = 'pages/projets/projets_publics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_white_text'] = False
        context['section_title'] = 'Projets'
        context['section_item_title'] = 'Projets publiés'
        return context


class NouveauProjetView(TemplateView):
    template_name = 'pages/projets/creation_projet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projet_active'] = True
        context['has_white_text'] = False
        context['section_title'] = 'Projets'
        context['section_item_title'] = 'Creation d\'un projet'
        return context


class ConsulterProjetView(TemplateView):
    template_name = 'pages/projets/detail_projet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_white_text'] = False
        context['section_title'] = 'Projets'
        context['section_item_title'] = 'Consultation projet'
        return context


class ModifierProjetView(TemplateView):
    template_name = 'pages/projets/detail_projet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_white_text'] = False
        context['section_title'] = 'Projets'
        context['section_item_title'] = 'Mise à jour projet'
        return context


class ListeProjetView(TemplateView):
    template_name = 'pages/projets/liste_projet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_white_text'] = False
        context['section_title'] = 'Projets'
        context['section_item_title'] = 'Listes des projets'
        return context