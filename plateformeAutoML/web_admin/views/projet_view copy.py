from pyexpat import model
from select import select
from statistics import mode
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from django.http import  JsonResponse
from django.conf import settings
import time, os, json
from django.template.loader import render_to_string
import traceback
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from web_admin.utils.file import *
from web_admin.enum import EEtatPublication, ENatureValeur
from web_admin.models import Algorithme, Projet, Fichier, Metrique, AlgorithmeProjet,Modele,JeuDonnees, Colonne, Imputation, MiseEchelle, Encodage, TableModel
from web_admin.utils.dataset import info_dataset, hist_img, load_dataframe
from web_admin.services import fetch_config as fetch

ALLOWED_EXTENSIONS = set(["npy", "csv", "xls", "xlsx"])

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

class ListeProjetView(TemplateView):
    template_name = 'pages/projets/liste_projet.html'

    def get_context_data(self, **kwargs):
        
        projets = Projet.objects.all().order_by('-id')

        context = super().get_context_data(**kwargs)
        context['has_white_text'] = False
        context['section_title'] = 'Projets'
        context['section_item_title'] = 'Listes des projets'
        context['projets'] = projets
        return context

def projet_update(request):
    return
    
def projet_delete(request, pk):
    if request.method == 'GET':
        Projet.objects.get(pk=pk).delete()
        return JsonResponse({'data': {}, 'transaction': {'code': 'success', 'titre':'Génial !!!', 'message': 'Projet supprimé avec success'}})
    else:
        return JsonResponse({'data': {}, 'transaction': {'code': 503, 'titre':'Oups !!!', 'message': 'Page non autorisée'}})


def projet_edit(request):
    return


def projet_detail(request,pk):
    template_name = 'pages/projets/projet_detail.html'
    
    projet = Projet.objects.get(pk=pk)

    algorithme_pro = AlgorithmeProjet.objects.filter(projet=projet.pk)
    print("---------------------------")
    print(algorithme_pro)

    models_projet = []

    for algo in list(algorithme_pro):
        print("-----------------",algo.pk)
        model_courent = Modele.objects.get(algorithme_projet = algo)

        print("--------ccc-------",model_courent)

        models_projet.append(model_courent)
    
    

        #print("xxxxxxxxxxxxxxxxxxx",model_courent.precision,model_courent.algorithme_projet.code)

    #modeles = model = Modele.objects.filter()
    modeles = ""

    context = dict()
    context['has_white_text'] = False
    context['section_title'] = 'Projets'
    context['section_item_title'] = 'Consultation projet'
    context['projet'] = projet
    context['modeles'] = models_projet
    return render(request, template_name, context=context)

class MesFavorisView(TemplateView):
    template_name = 'pages/projets/mes_favoris.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_white_text'] = False
        context['section_title'] = 'Mon espace'
        context['section_item_title'] = 'Mes favoris'
        return context
