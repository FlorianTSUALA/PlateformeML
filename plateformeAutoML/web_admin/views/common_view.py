from django.shortcuts import render
from django.urls import reverse_lazy
from web_admin.models import Algorithme
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from pyexpat import model
from select import select
from statistics import mode
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import HttpRequest, JsonResponse, HttpResponseRedirect
from django.conf import settings
import time, os, json
from django.template.loader import render_to_string
from matplotlib.pyplot import axis
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from web_admin.utils.file import *
from web_admin.enum import EEtatPublication, ENatureValeur
from web_admin.models import Algorithme, Projet, Fichier, Metrique, AlgorithmeProjet,Modele,JeuDonnees, Colonne, Imputation, MiseEchelle, Encodage, TableModel
from web_admin.utils.dataset import info_dataset, hist_img, load_dataframe
from web_admin.services import fetch_config as fetch

#IMPORT BIBLIOTHEQUE OF ML
from core_automl.bibliotheque.RMFrameClasse.refractoryFramwork import *
from core_automl.bibliotheque.RMFrameClasse.refractoryFramwork import estimator
from core_automl.bibliotheque.RMFrameClasse.refractoryFramwork.pretraitement import  PreprocessingData
from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder
from core_automl.bibliotheque.RMFrameClasse.ressources.algorithme import ALGORITHME_SYSTEME
from sklearn.pipeline import make_pipeline


ALLOWED_EXTENSIONS = set(["npy", "csv", "xls", "xlsx"])

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def liste_projet(request):
    projets = Projet.objects.all().order_by('-id')
    algorithmes = Algorithme.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    paginator = Paginator(projets, 10)
    try:
        projets = paginator.page(page)
    except PageNotAnInteger:
        projets = paginator.page(1)
    except EmptyPage:
        projets = paginator.page(paginator.num_pages)
    return render(request, 'pages/vitrine.html',{'algorithmes' : algorithmes,'has_white_text': False,'section_title' : 'projets','section_item_title' : 'Listes des projets','projets' :  projets})


class VitrineView(TemplateView):
    pass
    # template_name = 'pages/vitrine.html'
    # def get_context_data(self, **kwargs):
        
    #     projets = Projet.objects.all().order_by('-id')
    #     algorithmes = Algorithme.objects.all().order_by('-id')
        

    #     context = super().get_context_data(**kwargs)
    #     context['has_white_text'] = False
    #     context['section_title'] = 'Projets'
    #     context['section_item_title'] = 'Listes des projets'
    #     context['projets'] = projets
    #     context['algorithmes'] = algorithmes
    #     return context

def search_projets(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        print(search_str)
        print(len(Projet.objects.filter(titre__istartswith = search_str)))
        projets = Projet.objects.filter(titre__istartswith = search_str)
        data = projets.values()
        print(data)
        return JsonResponse(list(data),safe=False)
        

def groupe_algorithme(request):
    if request.method == "POST":
        algorith = request.POST.get('algorithme')
        # projetss = algorith.Projet.objects.all().order_by('-id')
        algorithme = Algorithme.objects.get(libelle = algorith)
        projets = AlgorithmeProjet.objects.filter(algorithme_id = algorithme.id) 
        algorithmes = Algorithme.objects.all().order_by('-id')
        print(algorithme.id)
        print(len(projets))
        print(len(algorithmes))
        for p in projets:
            print(p.algorithme.code)
       
        return render(request, 'pages/vitrine.html',{'algorithmes' : algorithmes,'has_white_text': False,'section_title' : 'Projets','section_item_title' : 'Listes des projets','projets' :  projets})  

# def groupe_algorithme(request,**kwargs):
#     template_name = 'pages/vitrine.html'
       
#     if request.method == "POST":
#         algorithme = request.POST.get('algorithme')
#         # projets = Projet.objects.all().order_by('-id')
#         algorithme = Algorithme.objects.get(libelle = algorithme)
#         projets = AlgorithmeProjet.objects.filter(id = algorithme.id) 
#         algorithmes = Algorithme.objects.all().order_by('-id')
#         context = get_context_data(**kwargs)
#         context['has_white_text'] = False
#         context['section_title'] = 'Projets'
#         context['section_item_title'] = 'Listes des projets'
#         context['projets'] = projets
#         context['algorithmes'] = algorithmes
#         return context
        
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


