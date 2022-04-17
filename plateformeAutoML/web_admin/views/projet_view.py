from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import JsonResponse
from django.conf import settings
import time, os
from django.template.loader import render_to_string
from web_admin.models import Algorithme, Projet
import pandas as pd
from web_admin.models import Fichier
from web_admin.enum import EEtatPublication
from web_admin.utils.file import *
from django.contrib.auth.decorators import login_required

# from web_admin.utils.session import *
from web_admin.utils.dataset import info_dataset, load_dataframe
from web_admin.services import fetch_config as fetch

ALLOWED_EXTENSIONS = set(["npy", "csv", "xls", "xlsx"])

# @login_required
class NouveauProjetView(View):

    def find_longest_word(self, mylist):
    	return max(mylist, key=len)

    def add_space(self, word, max):
        word = word.ljust(max, ' ')
        return word

    def padding(self, mydict, max):
        new_dict = { k:self.add_space(v, max) for k, v in mydict.items() }
        return new_dict.items()

    def get(self, request, *args, **kwargs):
        size = max( len(self.find_longest_word(fetch.get_nature_valeur())), len(self.find_longest_word(fetch.get_taxonomie_type_donnee())), 
                    len(self.find_longest_word(fetch.get_encodage())),len(self.find_longest_word(fetch.get_mise_echelle())), 
                    len(self.find_longest_word(fetch.get_imputation())))
        context = {
            'projt_active': True,
            'section_title': 'Projets',
            'section_item_title': 'Creation d\'un projet',
            'algorithmes': fetch.get_algorithme(),
            'nature_valeur': self.padding(fetch.get_nature_valeur(), size),
            'taxonomie_type_donnee': self.padding(fetch.get_taxonomie_type_donnee(), size),
            'encoder': self.padding(fetch.get_encodage(), size),
            'scaller': self.padding(fetch.get_mise_echelle(), size),
            'imputer': self.padding(fetch.get_imputation(), size),
            'status': EEtatPublication.choices(),
        }
        return render(request, 'pages/projets/creation_projet.html', context=context)
     
def get_algorithme_by_task(request):
    data = dict()
    if request.method == 'POST':
        task = request.POST.get('task', 'SUPERVISED')
        if task is not None:
            data = fetch.get_allgorithme_by_task(task)
        return JsonResponse({'data': data, 'transaction': {'code': 200, 'titre':'Génial !!!', 'message': 'Information enregistrée avec success'}})
    return JsonResponse({'data': data, 'transaction': {'code': 503, 'titre':'Oups !!!', 'message': 'Page non autorisée'}})


def load_initial(path, sep=','):
    """ Encodes data and returns new data """
    data = load_dataframe(path)
    mask = data.dtypes==object
    #get_categorical()
    categorical = data.columns[mask].tolist()
    print(categorical)
    if categorical:
        print("crash")
        #Encoder foreach column
        le = LabelEncoder()
        data[categorical] = data[categorical].apply(lambda x: le.fit_transform(x.astype(str)))
        data.to_csv(path, index=False)
    print("Not crash")
    return data

def featur_pg():

    values = session.get('values', 'not set')
    path = os.path.join(app.config['UPLOAD_FOLDER'],
                        session.get("filename", "not set"))
    data = load_initial(path,sep=values["sep"])
    empty_cols = [col for col in data.columns if data[col].isnull().all()]
    
    data.drop(empty_cols, axis=1, inplace=True)

    dropped_msg=""

    if empty_cols:
        dropped_msg = "Empty columns detected, dropped columns : "+str(empty_cols) 
    features = data.columns
    for i in range(len(features)):
        plt.clf()
        data[features[i]].hist()
        plt.savefig("static/images/figs/" + str(i),
                    bbox_inches="tight", transparent=True)
    return render_template("features.html", FEATURES=features, dropped_msg=dropped_msg)

def save_projet_info(request):
    if request.method == "POST":
        # print(request.POST)
        # return JsonResponse({'data':{'project_id': project_id, 'transaction': {'code': 200, 'titre':'Génial !!!', 'message': 'Information enregistrée avec success'}}})
        if request.user.is_authenticated:
            username = request.user.utilisateur.nom
            print('USERNAME : ', username)

        print( request.user.utilisateur.pk)
        data = {
            'titre': request.POST.get('titre'),
            'description': request.POST.get('description'),
            'mots_cles': request.POST.get('mots_cles'),
            'statut': request.POST.get('statut'),
            'image': request.FILES.get('image'),
            'utilisateur_id': request.user.utilisateur.pk,
        }
        print(data)
        project, created = Projet.objects.update_or_create( pk=request.POST.get('project_id', 0), defaults=data,)
        project_id = project.id
       
        # nombre_modele = request.POST.get('nombre_modele', 0)
        # print(_type)
        # if project_id == 0:
        #     projet = Projet(
        #                 titre = titre,
        #                 description = description,
        #                 mots_cles = mots_cles,
        #                 image = image,
        #                 statut = statut,
        #                 # est_publique = est_publique,
        #                 # nombre_modele = nombre_modele,
        #             )
        #     projet.save()
        #     project_id = projet.pk
        # else:
        #     projet = Projet.objects.get(pk=project_id)
        
        if request.session.get('project', None) is None:
            request.session['project'] = dict()
        request.session['project']['project_id'] = project_id
        return JsonResponse({'data':{'project_id': project_id,}, 'transaction': {'code': 200, 'titre':'Génial !!!', 'message': 'Information enregistrée avec success'}})


def save_preprocessing(request):

    if request.method == "POST":
        print(request.POST)
        return JsonResponse({'data': 'test'})
        title = request.POST.get('title')
        description = request.POST.get('description')
        metrique = request.POST.get('metrique')
        _type = request.POST.get('type')
        est_publique = request.POST.get('est_publique')
        nombre_modele = request.POST.get('nombre_modele')
        print(_type)
        project_id = request.POST.get('project_id', 0)
        if project_id == 0:
            projet = Projet(
                        title = title,
                        description = description,
                        metrique = metrique,
                        type = _type,
                        est_publique = est_publique,
                        nombre_modele = nombre_modele,
                    )
            projet.save()
            project_id = projet.pk
        else:
            projet = Projet.objects.get(pk=project_id)
        
        request.session['projet_id'] = project_id
        return JsonResponse({'data':{'project_id': project_id, 'transaction': {'code': 200, 'titre':'Génial !!!', 'message': 'Information enregistrée avec success'}}})
#TODO
def save_selection_variable(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        metrique = request.POST.get('metrique')
        _type = request.POST.get('type')
        est_publique = request.POST.get('est_publique')
        nombre_modele = request.POST.get('nombre_modele')
        print(_type)
        project_id = request.POST.get('project_id', 0)
        if project_id == 0:
            projet = Projet(
                        title = title,
                        description = description,
                        metrique = metrique,
                        type = _type,
                        est_publique = est_publique,
                        nombre_modele = nombre_modele,
                    )
            projet.save()
            project_id = projet.pk
        else:
            projet = Projet.objects.get(pk=project_id)
        
        request.session['projet_id'] = project_id
        return JsonResponse({'data':{'project_id': project_id, 'transaction': {'code': 200, 'titre':'Génial !!!', 'message': 'Information enregistrée avec success'}}})

def save_selection_algorithme(request):
    if request.method == "POST":
        data = dict()
        data['script'] = render_to_string('pages/projets/feature_chart.html', { 'data': 'hello Florian!!!' })
        return JsonResponse(data)

        title = request.POST.get('title')
        description = request.POST.get('description')
        metrique = request.POST.get('metrique')
        _type = request.POST.get('type')
        est_publique = request.POST.get('est_publique')
        nombre_modele = request.POST.get('nombre_modele')
        print(_type)
        project_id = request.POST.get('project_id', 0)
        if project_id == 0:
            projet = Projet(
                        title = title,
                        description = description,
                        metrique = metrique,
                        type = _type,
                        est_publique = est_publique,
                        nombre_modele = nombre_modele,
                    )
            projet.save()
            project_id = projet.pk
        else:
            projet = Projet.objects.get(pk=project_id)
        
        request.session['projet_id'] = project_id
        return JsonResponse({'data':{'project_id': project_id, 'transaction': {'code': 200, 'titre':'Génial !!!', 'message': 'Information enregistrée avec success'}}})

def upload_dataset(request):
    ts = time.gmtime()
    ts = time.strftime("__%Y_%m_%d__%H_%M_%S", ts)
    if request.method == 'POST':  
        fichier = request.FILES['file'].read()
        nom_fichier = request.POST['filename']
        ext = file_extention(nom_fichier)
        nom_fichier = str(nom_fichier).replace(ext, '') + ts + ext
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
                print(request.session.get('project', {}))
                old_file_id = request.session.get('project', {}).get('fichier_id', 0)
                if old_file_id != 0:
                    filename = Fichier.objects.get(pk=old_file_id).nom

                    media_root = getattr(settings, 'MEDIA_ROOT', 0)
                    path_file = os.path.join(media_root, filename)
                    if os.path.isfile(path_file):
                        os.remove(path_file)

                    Fichier.objects.filter(id=old_file_id).delete()
                request.session['fichier_id'] = FileFolder.pk
                
                if int(end):
                    cols_info, df = info_dataset(path)
                    res = JsonResponse({
                        'msg':'Chargment effectué avec success',
                        'cols_info': cols_info, 
                        'df': df.to_json(orient="split"), 
                        'chemin': chemin,
                    })
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
                            cols_info, df = info_dataset(model_id.chemin)
                            res = JsonResponse({
                                'msg':'Chargement effectué avec success',
                                'cols_info': cols_info, 
                                'df': df.to_json(orient="split"),
                                'chemin': model_id.chemin, 
                            })
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

def clean_session_project_creation(request):
    if request.method == "POST":
        request.session.clear()
        res = JsonResponse({'data':'Bye'})
        return res

class ListeProjetView(TemplateView):
    template_name = 'pages/projets/liste_projet.html'

    def get_context_data(self, **kwargs):
        
        projet = Projet.objects.all().order_by('-id')

        print("xxx",projet[0].image)

        context = super().get_context_data(**kwargs)
        context['has_white_text'] = False
        context['section_title'] = 'Projets'
        context['section_item_title'] = 'Listes des projets'
        context['projet'] = projet
        return context

        project_id = request.POST.get('project_id', 0)

        if project_id == 0:
            projet = Projet(
                        title = title,
                        description = description,
                        metrique = metrique,
                        type = type,
                        est_publique = est_publique,
                        nombre_modele = nombre_modele,
                    )
            projet.save()
            project_id = projet.pk
        else:
            projet = Projet.objects.get(pk=project_id)
    
        request.session['projet_id'] = project_id
        return JsonResponse({'data':{'project_id': project_id, 'msg':'Information enregistré avec success'}})
    

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


class ConsulterProjetView(TemplateView):
    template_name = 'pages/projets/detail_projet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_white_text'] = False
        context['section_title'] = 'Projets'
        context['section_item_title'] = 'Consultation projet'
        return context

class MesFavorisView(TemplateView):
    template_name = 'pages/projets/mes_favoris.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_white_text'] = False
        context['section_title'] = 'Mon espace'
        context['section_item_title'] = 'Mes favoris'
        return context

class ModifierProjetView(TemplateView):
    template_name = 'pages/projets/detail_projet.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_white_text'] = False
        context['section_title'] = 'Projets'
        context['section_item_title'] = 'Mise à jour projet'
        return context

