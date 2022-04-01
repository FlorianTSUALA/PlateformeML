from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import JsonResponse
from django.conf import settings
import time

from web_admin.models import Algorithme
import pandas as pd
from web_admin.models import Fichier

# Create your views here.
from .utils_local import *



ALLOWED_EXTENSIONS = set(["npy", "csv", "xls", "xlsx"])

def save_info_projet(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        metrique = request.POST.get('metrique')
        type = request.POST.get('type')
        est_publique = request.POST.get('est_publique')
        nombre_modele = request.POST.get('nombre_modele')
    
        id = request.POST.get('id', None)
        if id is not None:
            projet = Projet(
                        title = title,
                        description = description,
                        metrique = metrique,
                        type = type,
                        est_publique = est_publique,
                        nombre_modele = nombre_modele,
                    )
            projet.save()
            id = projet.pk
        else:
            projet = Projet.objects.get(pk=id)
            #update projet info
        return JsonResponse({'data':{'id': id, 'message':'Information enregistré avec success'}})
    
def upload_dataset(request):
    ts = time.gmtime()
    ts = time.strftime("__%Y_%m_%d__%H_%M_%S", ts)

    if request.method == 'POST':  
        fichier = request.FILES['file'].read()
        nom_fichier = request.POST['filename'] + ts
        chemin = request.POST['path']
        end = request.POST['end']
        nextSlice = request.POST['nextSlice']
        if fichier=="" or nom_fichier=="" or chemin=="" or end=="" or nextSlice=="":
            res = JsonResponse({'data':'Requete invalide'})
            return res
        else:
            if chemin == 'null':
                path = 'media/' + nom_fichier
                with open(path, 'wb+') as destination: 
                    destination.write(fichier)
                FileFolder = Fichier()
                FileFolder.chemin = nom_fichier 
                FileFolder.eof = end
                FileFolder.nom = nom_fichier
                FileFolder.save()

                old_file_id = request.session.get('fichier_id', None)
                if old_file_id is not None:
                    filename = Fichier.objects.get(pk=old_file_id).nom

                    media_root = getattr(settings, 'MEDIA_ROOT', None)
                    path_file = os.path.join(media_root, filename)
                    if os.path.isfile(path_file):
                        os.remove(path_file)

                    Fichier.objects.filter(id=old_file_id).delete()
                request.session['fichier_id'] = FileFolder.pk
                
                if int(end):
                    data = load_dataframe(path)
                    res = JsonResponse({'data':'Chargment effectué avec success','chemin': nom_fichier})
                else:
                    res = JsonResponse({'chemin': nom_fichier})
                return res

            else:
                path = 'media/' + chemin
                model_id = Fichier.objects.get(chemin=chemin)
                if model_id.nom == nom_fichier:
                    if not model_id.eof:
                        with open(path, 'ab+') as destination: 
                            destination.write(fichier)
                        if int(end):
                            model_id.eof = int(end)
                            model_id.save()
                            res = JsonResponse({'data':'Chargement effectué avec success','chemin':model_id.chemin})
                        else:
                            res = JsonResponse({'chemin':model_id.chemin})    
                        return res
                    else:
                        res = JsonResponse({'data':'EOF trouvé. Requeste invalide'})
                        return res
                else:
                    res = JsonResponse({'data':'Aucun fichier existant dans ce fichier'})
                    return res
    else:
        res = JsonResponse({'data':'Requete non authorisée'})
        return res

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