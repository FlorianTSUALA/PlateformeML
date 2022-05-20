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



class ListeProjetView(TemplateView):
    template_name = 'pages/projets/vitrine.html'

    def get_context_data(self, **kwargs):
        
        projets = Projet.objects.all().order_by('-id')

        context = super().get_context_data(**kwargs)
        context['has_white_text'] = False
        context['section_title'] = 'Projets'
        context['section_item_title'] = 'Listes des projets'
        context['projets'] = projets
        return context