from django.shortcuts import render
from django.urls import reverse_lazy
from web_admin.models import Algorithme
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import JsonResponse

class VitrineView(TemplateView):
    template_name = 'pages/vitrine.html'

class AccueilView(TemplateView):
    template_name = 'pages/accueil.html'

class FAQView(TemplateView):
    template_name = 'pages/faq.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_title'] = 'Autres'
        context['section_item_title'] = 'FAQ'
        return context


class AProposView(TemplateView):
    template_name = 'pages/apropos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_title'] = 'Autres'
        context['section_item_title'] = 'A Propos'
        return context


