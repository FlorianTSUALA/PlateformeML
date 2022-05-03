from pyexpat import model
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
from core_automl.bibliotheque.RMFrameClasse.refractoryFramwork import classification
from core_automl.bibliotheque.RMFrameClasse.refractoryFramwork.pretraitement import  PreprocessingData
from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder
from core_automl.bibliotheque.RMFrameClasse.ressources.algorithme import ALGORITHME_SYSTEME
from sklearn.pipeline import make_pipeline


ALLOWED_EXTENSIONS = set(["npy", "csv", "xls", "xlsx"])

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

def clean_session_projet_creation(request):
    del request.session['projet'] #.clear()
    if request.get('dataset', {}):
        Fichier.objects.all().delete()
        del request.session['dataset']#.clear()
    request.session.modified = True

class EditProjet(LoginRequiredMixin, View):

    def find_longest_word(self, mylist):
    	return max(mylist, key=len)

    def add_space(self, word, max):
        word = word.ljust(max, ' ')
        return word

    def padding(self, mydict, max):
        new_dict = { k:self.add_space(v, max) for k, v in mydict.items() }
        return new_dict.items()

    def get(self, request, *args, **kwargs):
        print('TAG : %s'%kwargs.get('tag', "-------------"))
        clean_session_projet_creation(request)
        size = max( len(self.find_longest_word(fetch.get_nature_valeur())), len(self.find_longest_word(fetch.get_taxonomie_type_donnee())), 
                    len(self.find_longest_word(fetch.get_encodage())),len(self.find_longest_word(fetch.get_mise_echelle())), 
                    len(self.find_longest_word(fetch.get_imputation())))

        models = {
            'random Forest': {
                'code' : 'xxxxx',
                'precision' : 67,
                'famille_algorithme' : 'Lineaire'
            },
            'regression Logistique': {
                'code' : 'xxxxx',
                'precision' : 37,
                'famille_algorithme' : 'Lineaire'
            },
            'Support vector machine': {
                'code' : 'xxxxx',
                'precision' : 69,
                'famille_algorithme' : 'Lineaire'
            },
            'Arbre binaire': {
                'code' : 'xxxxx',
                'precision' : 96,
                'famille_algorithme' : 'Nom Lineaire'
            },
        }

        liste_models = []

        for i in range(0,10):
            model = TableModel(i,'algo_'+str(i),'code_'+str(i), 10*i+50,'famille_'+str(i))
            liste_models.append(model)

        context = {
            'projt_active': True,
            'section_title': 'Projets',
            'section_item_title': 'Creation d\'un projet',
            'algorithmes': fetch.get_algorithme(),
            'taches': fetch.get_tache_algorithme(),
            # 'taches': fetch.get_tache(True),
            'type_apprentissages': fetch.get_type_apprentissage_tache(),
            'metriques': json.dumps(fetch.get_metrique(True)),
            'tache_algorithmes': json.dumps(fetch.get_tache_algorithme(True)),
            'type_apprentissage_taches': json.dumps(fetch.get_type_apprentissage_tache(True)),
            'nature_valeur': self.padding(fetch.get_nature_valeur(), size),
            'taxonomie_type_donnee': self.padding(fetch.get_taxonomie_type_donnee(), size),
            'encoder': self.padding(fetch.get_encodage(), size),
            'scaller': self.padding(fetch.get_mise_echelle(), size),
            'imputer': self.padding(fetch.get_imputation(), size),
            'status': EEtatPublication.choices(),
            'models':liste_models
        }
        return render(request, 'pages/projets/creation_projet.html', context=context)
     
def get_algorithme_by_task(request):
    data = dict()
    if request.method == 'POST':
        task = request.POST.get('task', 'SUPERVISED')
        if task is not None:
            data = fetch.get_allgorithme_by_task(task)
        return JsonResponse({'data': data, 'transaction': {'code': 'success', 'titre':'Génial !!!', 'message': 'Information enregistrée avec success'}})
    return JsonResponse({'data': data, 'transaction': {'code': 503, 'titre':'Oups !!!', 'message': 'Page non autorisée'}})

def projet_info(request):
    if request.method == "POST":
        data = {
            'titre': request.POST.get('titre'),
            'description': request.POST.get('description'),
            'mots_cles': request.POST.get('mots_cles'),
            'statut': request.POST.get('statut'),
            'image': request.FILES.get('image'),
            'utilisateur_id': request.user.utilisateur.pk,
        }

        projet = None
        projet_id = request.POST.get('projet_id', '0')

        if projet_id == '0':
            print('create')
            projet = Projet(
                        titre = data['titre'],
                        description = data['description'],
                        mots_cles = data['mots_cles'],
                        image = data['image'],
                        statut = data['statut'],
                        utilisateur_id = data['utilisateur_id'],
                    )
            projet.save()
        else:
            print('update')
            projet = Projet.objects.get(pk=projet_id)
            projet.titre = data['titre']
            projet.description = data['description']
            projet.mots_cles = data['mots_cles']
            projet.image = data['image']
            projet.statut = data['statut']
            projet.utilisateur_id = data['utilisateur_id']
            projet.save()
        projet_id = projet.pk

        if request.session.get('projet', None) is None:
            request.session['projet'] = dict()
        request.session['projet']['projet_id'] = projet_id
        return JsonResponse({'data':{'projet_id': projet_id,}, 'transaction': {'code': 'success', 'titre':'Génial !!!', 'message': 'Information enregistrée avec success'}})
    else:
        projet_session = request.session.get('projet', None)
        if projet_session is not None:
            projet = Project.objects.get(pk=projet_session.get('projet_id', 0))
            return JsonResponse({'data':json.dumps(projet), 'transaction': {'code': 'success', 'titre':'Génial !!!', 'message': 'Information enregistrée avec success'}})

def info_preprocessing(request):
    print('info_preprocessing')
    if request.method == "POST":
        print('POST')
        preprocessing = json.loads((list(request.POST.keys())[0]))['preprocessing']
        selected = json.loads((list(request.POST.keys())[0]))['selected']

        jeu_donnees = None
        if not request.session.get('projet', {}):
            return JsonResponse({'data':{}, 'transaction': {'code': 'success', 'titre':'Oups', 'message': 'Veuillez d\'abord enregistrer les informations du projet'}})
        if not request.session.get('dataset', {}):
            return JsonResponse({'data':{}, 'transaction': {'code': 'success', 'titre':'Oups', 'message': 'Veuillez d\'abord Charger un jeu de données'}})

        projet_id = request.session.get('projet').get('projet_id', 0)
        jeu_donnees, created = JeuDonnees.objects.get_or_create(projet_id=projet_id)
        file_id = request.session.get('dataset').get('fichier_id', 0)
        print(file_id)
        _fichier = Fichier.objects.get(pk=file_id)
        jeu_donnees.fichier = _fichier.chemin
        jeu_donnees.save()
        Colonne.objects.filter(jeu_donnees=jeu_donnees).delete()
        df = pd.read_json(request.session['dataset']['df'])
        # print(preprocessing)
        for item in preprocessing:
            #item['nature'] not found skip : colvis
            valeurs = ''
            print('item : ', item)
            if item['nature'] == ENatureValeur.QUALITATIF.value:
                _valeurs = df[item['column']].unique()
                valeurs = ','.join(map(str, _valeurs))
                print(_valeurs, valeurs)

            colonne = Colonne()
            colonne.libelle=item['column']
            type_donnees=item['type']
            colonne.est_categoriel=(item['nature'] == ENatureValeur.QUALITATIF.value)
            colonne.est_target=False
            colonne.est_selectionnee=(item['column'] in selected)
            colonne.pattern=''
            colonne.valeurs=valeurs
            colonne.jeu_donnees=jeu_donnees
            colonne.encodage=Encodage.objects.get_or_none(code=item['encoder'])
            colonne.imputation=Imputation.objects.get_or_none(code=item['imputer'])
            colonne.normalisation=MiseEchelle.objects.get_or_none(code=item['scaller'])
            colonne.save()
            print(colonne.pk)

        cols_info = request.session['dataset']['cols_info'] #todo check db info
       # context = {'images': hist_img(df, cols_info).items()}
        context = {}
        return JsonResponse({
                                'data':{'img_block': render_to_string('pages/projets/fragment/block/histogramme.html', context=context, request=request )}, 
                                'transaction': {'code': 'success', 'titre':'Génial !!!', 'message': 'Information enregistrée avec success'}
                            })
    else:
        return JsonResponse({'data':{}, 'transaction': {'code': 'error', 'titre':'Oups !!!', 'message': 'Requete non autorisée'}})


def selection_algorithme(request):
    if request.method == "POST":
        jeu_donnees = None
        if request.session.get('projet', None) is None:
            return JsonResponse({'data':{}, 'transaction': {'code': 'success', 'titre':'Oups', 'message': 'Veuillez d\'abord enregistrer les informations du projet'}})
        projet_id = request.session.get('projet').get('projet_id')

        #--------Begin Save target
        jeu_donnees, created = JeuDonnees.objects.get_or_create(projet_id=projet_id)
        target = request.POST.get('target', 'non défini')
        if target != 'non défini':
            colonne = Colonne.objects.get(jeu_donnees=jeu_donnees, libelle=target)
            colonne.est_target = True
            colonne.save()
        #--------End Save target
        
        algos = request.POST.getlist('algo[]')
        _metrique = request.POST.get('metrique')
        #to_review
        metrique = Metrique.objects.get(code=_metrique)
        #todo get default metrique from task if doesn't exist
        tache = request.POST.get('tache')

        AlgorithmeProjet.objects.filter(projet_id=request.session.get('projet', {}).get('projet_id', 0)).delete()
        for item in algos:
            algorithme = Algorithme.objects.get(code=item)
            AlgorithmeProjet.objects.create(projet_id=request.session.get('projet', {}).get('projet_id', 0), algorithme=algorithme, metrique=metrique)
        return JsonResponse({'data':'', 'transaction': {'code': 'success', 'titre':'Génial !!!', 'message': 'Algorithmes enregistrés avec success'}})
    else:
        items = AlgorithmeProjet.objects.filter(projet_id=request.session.get('projet', {}).get('projet_id', 0))
        data = dict()
        data['algorithmes'] = set()
        for item in items:
            data['algorithmes'].add(item.algorithme.code)
        data['metrique'] = algorithme_projet.metrique.code 
        return JsonResponse({'data': json.dumps(data), 'transaction': {'code': 'success', 'titre':'Génial !!!', 'message': 'Chargement des informations sur le choix des algorithmes'}})

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
            return JsonResponse({'data':{}, 'transaction': {'code': 'error', 'titre':'Oups !!!', 'message': 'Requete invalide'}})
        else:
            if chemin == 'null':
                path = 'media/' + nom_fichier
                with open(path, 'wb+') as destination: 
                    destination.write(fichier)
                _fichier = Fichier()
                _fichier.chemin = nom_fichier 
                _fichier.eof = end
                _fichier.nom = nom_fichier
                _fichier.save()
                # print('dataset : ', request.session.get('dataset'))
                if not request.session.get('dataset', {}):
                    request.session['dataset'] = dict()
                old_file_id = request.session.get('dataset').get('fichier_id', 0)
                print(old_file_id, nom_fichier)
                if old_file_id:
                    #to_review
                    filename = Fichier.objects.get(pk=old_file_id).nom

                    media_root = getattr(settings, 'MEDIA_ROOT', 0)
                    path_file = os.path.join(media_root, filename)
                    if os.path.isfile(path_file):
                        os.remove(path_file)
                    # request.session['dataset']['fichier_id'] = _fichier.pk
                    Fichier.objects.get(pk=old_file_id).delete()
                request.session['dataset']['fichier_id'] = _fichier.pk
                request.session.modified = True
                print(request.session['dataset']['fichier_id'])
                
                if int(end):
                    cols_info, df = info_dataset(path)
                    context = {'images':  hist_img(df, cols_info).items()}
                    request.session['dataset']['df'] = df.to_json()
                    request.session['dataset']['cols_info'] = cols_info

                    res = JsonResponse({'data':{
                        'cols_info': cols_info, 
                        'df': df.to_json(orient="split"), 
                        'chemin': chemin,
                        'img_block': render_to_string('pages/projets/fragment/block/histogramme.html', context, request=request),
                    }, 'transaction': {'code': 'success', 'titre':'Cool !!!', 'message': 'Chargment effectué avec success'}})
                else:
                    res = JsonResponse({'data':{'chemin': nom_fichier}, 'transaction': {'code': 'success', 'titre':'En cours !!!', 'message': 'Chargment en cours'}})
            else:
                print('---------')
                print('---------')
                print('---------')
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
                            context = {'images':  hist_img(df, cols_info).items()}
                            request.session['ddataset']['df'] = df.to_json()
                            request.session['ddataset']['cols_info'] = cols_info

                            res = JsonResponse({'data':{
                                                        'cols_info': cols_info, 
                                                        'df': df.to_json(orient="split"), 
                                                        'chemin': chemin,
                                                        'img_block': render_to_string('pages/projets/fragment/block/histogramme.html', context, request=request),
                            }, 'transaction': {'code': 'success', 'titre':'Cool !!!', 'message': 'Chargment effectué avec success'}})
                        else:
                            res = JsonResponse({'data':{'chemin': model_id.chemin}, 'transaction': {'code': 'success', 'titre':'En cours !!!', 'message': 'Chargment en cours'}})
                    else:
                        res = JsonResponse({'data':{}, 'transaction': {'code': 'error', 'titre':'Oups !!!', 'message': 'EOF trouvé. Requeste invalide'}})
                else:
                    res = JsonResponse({'data':{}, 'transaction': {'code': 'error', 'titre':'Oups !!!', 'message': 'Aucun fichier existant dans ce fichier'}})
    else:
        res = JsonResponse({'data':{}, 'transaction': {'code': 'error', 'titre':'Oups !!!', 'message': 'Requete non autorisée'}})
    return res

def clean_session_projet_creation(request):
    if request.method == "POST":
        request.session.clear()
        return JsonResponse({'data':{}, 'transaction': {'code': 'info', 'titre':'Bye !!!', 'message': 'End of session in this page'}})

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


def projet_detail(request, id):
    template_name = 'pages/projets/detail_projet.html'
    context = dict()
    context['has_white_text'] = False
    context['section_title'] = 'Projets'
    context['section_item_title'] = 'Consultation projet'
    
    return render(request, template_name, context=context)


class MesFavorisView(TemplateView):
    template_name = 'pages/projets/mes_favoris.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_white_text'] = False
        context['section_title'] = 'Mon espace'
        context['section_item_title'] = 'Mes favoris'
        return context

def train_models(request):

    if request.method == "POST":

        
        jeu_donnees = None
        if not request.session.get('projet', {}):
            return JsonResponse({'data':{}, 'transaction': {'code': 'success', 'titre':'Oups', 'message': 'Veuillez d\'abord enregistrer les informations du projet'}})
        if not request.session.get('dataset', {}):
            return JsonResponse({'data':{}, 'transaction': {'code': 'success', 'titre':'Oups', 'message': 'Veuillez d\'abord Charger un jeu de données'}})

        df = pd.read_json(request.session['dataset']['df'])

        projet_id = request.session.get('projet').get('projet_id', 0)
        jeu_donnees = JeuDonnees.objects.get(projet_id=projet_id)
        jeu_donnees.pourcentage_validation = request.POST['p_val']
        jeu_donnees.pourcentage_test = request.POST['p_test']
        jeu_donnees.pourcentage_entrainement = request.POST['p_train']
        jeu_donnees.taille = len(df)
        jeu_donnees.save()
        
        p_val = request.POST['p_val']
        p_train = request.POST['p_train'] 
        p_test = request.POST['p_test']
        #
        target = Colonne.objects.get_or_none(jeu_donnees=jeu_donnees, est_target=True)
        selected_columns = [item['libelle'] for item in Colonne.objects.get_or_none(jeu_donnees=jeu_donnees, est_selectionnee=True)]
        #remove all other columns
        new_df = df[df.columns.intersection(selected_columns)]

        technique_normalisation = StandardScaler()
        technique_encodage  = OneHotEncoder()
        imputation_valeur_num = "mean"
        imputation_valeur_cat = 'most_frequent'
        encodage_target = LabelEncoder()
        metric = 'f1' #Pas utilisé

        algorithms = AlgorithmeProjet.objects.get(projet_id=projet_id)

        training_algorithms_pipeline = {}
        for algorithm in algorithms:
            pipeline_pretraitement = PreprocessingData(
                    df_dataset, target, strategy_val_manquante_num = imputation_valeur_num, methode_normalisation=technique_normalisation, 
                    strategy_val_manquante_cat=imputation_valeur_cat, methode_encodage=technique_encodage
            )
            preprocessor = pipeline_pretraitement.pipelinePreprocessing()

            initialisation_algo = ALGORITHME_SYSTEME[algorithm.algorithme.code]['init']
            hyperparametre_algo = ALGORITHME_SYSTEME[algorithm.algorithme.code]['hyperparametre']
            pipeline_algo = make_pipeline(preprocessor, initialisation_algo)
            training_algorithms_pipeline[algorithm.algorithme.code] = [pipeline_algo,hyperparametre_algo]

        classement = classification.Classification(training_algorithms_pipeline, dataset, target)
        """
            path = 'media/' + nom_model #projet_id_algo_day
                with open(path, 'wb+') as destination: 
                    destination.write(fichier)
        """
        print(training_algorithms_pipeline)
        #performences_models, best_model, model_, precision_ = classement.executer()
        #performences_models, models_fit, precision_best,name_= classement.executer()
        #print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",precision_)
        base_model = ''
        precision = 100
        try:
            dico_infos_train = {}
            for algo in algorithms:
                #base_model,precision = classement.optimisationHyperParam(algo,scoring=metric, cv=10)

                #chemin = classement.save_model(base_model, model.pk)
                """dico_infos_train[algo] = {
                    model : base_model,
                    precision : precision 
                }"""
        except:
            print("ERREUR lors c l'entrainement ddes  model")

        print(dico_infos_train)
                    
        liste_models = []
        for index, algo in  enumerate(algorithms):
            libele_algo = ALGORITHME_SYSTEME[algo]['label']
            famille_algo = ALGORITHME_SYSTEME[algo]['family']
            model = TableModel(index, libele_algo, 'code_',precision*100, famille_algo)
            liste_models.append(model)

        print(liste_models)

        context = {
            'models':liste_models
        }
        return render(request, 'pages/projets/creation_projet.html', context=context)


def predict_model(request, pk):
    print('prediction...')
    if request.method == "POST":
        print('POST')
        jeu_donnees = None
        # return render(request, 'pages/projets/fragments/block/')
        if not request.session.get('projet', {}):
            return JsonResponse({'data':{}, 'transaction': {'code': 'success', 'titre':'Oups', 'message': 'Veuillez d\'abord enregistrer les informations du projet'}})
       # context = {'images': hist_img(df, cols_info).items()}
        context = {}
        return JsonResponse({
                                'data':{'img_block': render_to_string('pages/projets/fragment/block/histogramme.html', context=context, request=request )}, 
                                'transaction': {'code': 'success', 'titre':'Génial !!!', 'message': 'Information enregistrée avec success'}
                            })
    else:
        return JsonResponse({'data':{}, 'transaction': {'code': 'error', 'titre':'Oups !!!', 'message': 'Requete non autorisée'}})


def download_model(request, pk):
    if pk != '':
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Define the full file path
        filepath = BASE_DIR + '/filedownload/Files/' + filename
        # Open the file for reading content
        path = open(filepath, 'rb')
        # Set the mime type
        mime_type, _ = mimetypes.guess_type(filepath)
        # Set the return value of the HttpResponse
        response = HttpResponse(path, content_type=mime_type)
        # Set the HTTP header for sending to browser
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        # Return the response value
        return response
    else:
        # Load the template
        print('hello')
