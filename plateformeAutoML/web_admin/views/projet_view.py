from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import HttpRequest, JsonResponse
from django.conf import settings
import time, os, json
from django.template.loader import render_to_string
from matplotlib.pyplot import axis
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
#from plateformeAutoML.web_admin.models import JeuDonnees

from web_admin.utils.file import *
from web_admin.enum import EEtatPublication
from web_admin.models import Algorithme, Projet, Fichier, Metrique, AlgorithmeProjet,Modele,JeuDonnees
from web_admin.utils.dataset import info_dataset, load_dataframe
from web_admin.services import fetch_config as fetch

#IMPORT BIBLIOTHEQUE OF ML
from core_automl.bibliotheque.RMFrameClasse.refractoryFramwork import *
from core_automl.bibliotheque.RMFrameClasse.refractoryFramwork import classification
from core_automl.bibliotheque.RMFrameClasse.refractoryFramwork.pretraitement import  PreprocessingData
from sklearn.preprocessing import StandardScaler,OneHotEncoder,LabelEncoder
from core_automl.bibliotheque.RMFrameClasse.ressources.algorithme import ALGORITHME_SYSTEME
from sklearn.pipeline import make_pipeline

ALLOWED_EXTENSIONS = set(["npy", "csv", "xls", "xlsx"])

def clean_session_projet_creation(request):
    request.session['projet'].clear()

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


        """code = models.CharField(max_length=254, blank=True,null=True)
        chemin =  models.CharField(max_length=254, blank=True,null=True)
        precision =  models.CharField(max_length=254, blank=True,null=True)
        rapport = models.TextField(max_length=254, blank=True,null=True)
        resume = models.TextField(max_length=254, blank=True,null=True)
        algorithme_projet = models.ForeignKey(AlgorithmeProjet, on_delete=models.CASCADE)"""



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

        class Mod:
            def __init__(self,id,algo,code,precision,famille):
                self.id = id
                self.algo = algo
                self.code = code
                self.precision = precision
                self.famille = famille

        liste_models = []

        for i in range(0,10):

            mod = Modele()
            model = Mod(i,'algo_'+str(i),'code_'+str(i),2*i+50,'famille_'+str(i))
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
        return JsonResponse({'data':{'projet_id': projet_id,}, 'transaction': {'code': 200, 'titre':'Génial !!!', 'message': 'Information enregistrée avec success'}})


def save_preprocessing(request):

    if request.method == "POST":
        print(request.POST)
        return JsonResponse({'data': 'test'})
        title = request.POST.get('title')
        description = request.POST.get('description')
        # metrique = request.POST.get('metrique')
        _type = request.POST.get('type')
        est_publique = request.POST.get('est_publique')
        nombre_modele = request.POST.get('nombre_modele')
        print(_type)
        projet_id = request.POST.get('projet_id', 0)
        if projet_id == 0:
            projet = Projet(
                        title = title,
                        description = description,
                        metrique = metrique,
                        type = _type,
                        est_publique = est_publique,
                        nombre_modele = nombre_modele,
                    )
            projet.save()
            projet_id = projet.pk
        else:
            projet = Projet.objects.get(pk=projet_id)
        
        request.session['projet_id'] = projet_id
        return JsonResponse({'data':{'projet_id': projet_id, 'transaction': {'code': 200, 'titre':'Génial !!!', 'message': 'Information enregistrée avec success'}}})

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
        projet_id = request.POST.get('projet_id', 0)
        if projet_id == 0:
            projet = Projet(
                        title = title,
                        description = description,
                        metrique = metrique,
                        type = _type,
                        est_publique = est_publique,
                        nombre_modele = nombre_modele,
                    )
            projet.save()
            projet_id = projet.pk
        else:
            projet = Projet.objects.get(pk=projet_id)
        
        request.session['projet_id'] = projet_id
        return JsonResponse({'data':{'projet_id': projet_id, 'transaction': {'code': 200, 'titre':'Génial !!!', 'message': 'Information enregistrée avec success'}}})

def selection_algorithme(request):
    if request.method == "POST":
        algos = request.POST.getlist('algo[]')
        _metrique = request.POST.get('metrique')
        metrique = Metrique.objects.get(code=_metrique)
        #todo get default metrique from task if doesn't exist
        tache = request.POST.get('tache')

        AlgorithmeProjet.objects.filter(projet_id=request.session.get('projet').get('projet_id')).delete()
        for item in algos:
            algorithme = Algorithme.objects.get(code=item)
            AlgorithmeProjet.objects.create(projet_id=request.session.get('projet').get('projet_id'), algorithme=algorithme, metrique=metrique)
        return JsonResponse({'data':'', 'transaction': {'code': 200, 'titre':'Génial !!!', 'message': 'Algorithmes enregistrés avec success'}})
    else:
        items = AlgorithmeProjet.objects.filter(projet_id=request.session.get('projet').get('projet_id'))
        data = dict()
        data['algorithmes'] = set()
        for item in items:
            data['algorithmes'].add(item.algorithme.code)
        data['metrique'] = algorithme_projet.metrique.code 
        
        return JsonResponse({'data': json.dumps(data), 'transaction': {'code': 200, 'titre':'Génial !!!', 'message': 'Chargement des informations sur le choix des algorithmes'}})

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
                print(request.session.get('projet', {}))
                old_file_id = request.session.get('projet', {}).get('fichier_id', 0)
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

def clean_session_projet_creation(request):
    if request.method == "POST":
        request.session.clear()
        res = JsonResponse({'data':'Bye'})
        return res

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
    
def projet_delete(request):
    return
    
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
        
        p_val = request.POST['p_val']
        p_train = request.POST['p_train'] 
        p_test = request.POST['p_test']
        
       
        chemin = r'C:\Users\USER\Documents\ML\PlateformeML\plateformeAutoML\chunk.csv'

        dataset = pd.read_csv(chemin)

        #colonnes = Colonnne.objects.filter(dataset = datass)
        colonnes = dataset.columns

        #chemin = datass.source_dataset
        target = 'Churn'
        list_colonnes_select = list(colonnes)
        """for colonne in list(colonnes):
            list_colonnes_select.append(colonne.nom_colonne)"""


        dataframe = dataset.drop(['customerID'],axis=1)

        print("newwwwwwwwwwww",dataframe)


        #target = target


        dataset = dataframe
        colonne_witout_target = []
        for col in list_colonnes_select:
            if col !=target:
                colonne_witout_target.append(col)



        technique_normalisation = StandardScaler()
        technique_encodage  = OneHotEncoder()
        imputation_valeur_num = "mean"
        imputation_valeur_cat = 'most_frequent'
        encodage_target = LabelEncoder()
        metric = 'f1'

        preprocessor1 = PreprocessingData(dataset, target, strategy_val_manquante_num=imputation_valeur_num,
                                          methode_normalisation=technique_normalisation,
                                          strategy_val_manquante_cat=imputation_valeur_cat, methode_encodage=technique_encodage)

        label = preprocessor1.encodage_label(encodage_label=encodage_target)

        ##donnee transformees
        data_traiter, dataframeT = preprocessor1.transfom()


        dataset = preprocessor1.dataFrame
        preprocessor = preprocessor1.pipelinePreprocessing()

        ###################### INITIALISATION DES Algorithmes NECESSAIRES POUR LE SCORING #################
        #liste_algo = projet.analyse.algorithmes.all()
        
        #Algorithmechoisis = ["SVM","Logistic"]
        Algorithmechoisis = ["SVM"]
        print(Algorithmechoisis)


        dict_algo_choisis = {}
        for algo in Algorithmechoisis:
            initialisation_algo = ALGORITHME_SYSTEME[algo]['init']
            hyperparametre_algo = ALGORITHME_SYSTEME[algo]['hyperparametre']
            pipeline_algo = make_pipeline(preprocessor,initialisation_algo)
            dict_algo_choisis[algo] = [pipeline_algo,hyperparametre_algo]

        classement = classification.Classification(dict_algo_choisis, dataset, target)

        print(dict_algo_choisis)
        #performences_models, best_model, model_, precision_ = classement.executer()
        #performences_models, models_fit, precision_best,name_= classement.executer()
        #print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",precision_)
        
        try:
            dico_infos_train = {}
            for algo in Algorithmechoisis:
                base_model,precision = classement.optimisationHyperParam(algo,scoring=metric, cv=10)

                #chemin = classement.save_model(base_model, model.pk)
                """dico_infos_train[algo] = {
                    model : base_model,
                    precision : precision 
                }"""
        except:
            print("ERREUR lors c l'entrainement ddes  model")

        print(dico_infos_train)
   
        class Mod:
            def __init__(self,id,algo,code,precision,famille):
                self.id = id
                self.algo = algo
                self.code = code
                self.precision = precision
                self.famille = famille
                    
        liste_models = []
        for algo in Algorithmechoisis:

            libele_algo = ALGORITHME_SYSTEME[algo]['label']
            model = Mod(0,algo,'code_',precision*100,'famille_')
            liste_models.append(model)

        print(liste_models)

        context = {
            'models':liste_models
        }
        return render(request, 'pages/projets/creation_projet.html', context=context)


     
        





  




