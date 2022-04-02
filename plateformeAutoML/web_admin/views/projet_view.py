from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import JsonResponse
from django.conf import settings
import time, os

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
    
        id = request.POST.get('id', 0)
        if id == 0:
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
        request.session['projet_id'] = id
        return JsonResponse({'data':{'id': id, 'msg':'Information enregistré avec success'}})
    
"""def upload_dataset(request):
    ts = time.gmtime()
    #ts = time.strftime("__%Y_%m_%d__%H_%M_%S", ts)

    if request.method == 'POST':  
        fichier = request.FILES['file'].read()
        ext = os.path.splitest(request.POST['filename'])
        #nom_fichier = ext[0] + ts + ext[1] 
        print("-------------------->nom du fichier ",nom_fichier)
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
                    data = info_dataset(path)
                    res = JsonResponse({'msg':'Chargment effectué avec success','data': data, 'chemin': chemin})
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
                            data = info_dataset(model_id.chemin)
                            res = JsonResponse({'msg':'Chargement effectué avec success','data': data, 'chemin': model_id.chemin})
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

"""
#FONCTION EXTRACTION DES CARACTERISQUES D'UNE COLONNE
def infos_dataset(dataframe):

    columns = dataframe.columns
    liste_col = {}
    for col in columns:
        macolonne = {}
        macolonne["type"] = dataframe[col].dtype
        macolonne["data"] = list(dataframe[col])

        if (dataframe[col].dtype == "int64" or dataframe[col].dtype == "int32"):
            macolonne["scaler"] = "Standard_Scaler"
            macolonne["imputer"] = "Mean"
            macolonne["encoder"] = "None"
            if dataframe[col].count() < 10:
                macolonne["nature"] = "discret"
            else:
                macolonne["nature"] = "continue"

        elif (dataframe[col].dtype == "bool"):
            macolonne["scaler"] = "None"
            macolonne["imputer"] = "Most_frequent"
            macolonne["encoder"] = "OneHot_Encoder"

            macolonne["nature"] = "discret"
        else:
            macolonne["scaler"] = "None"
            macolonne["imputer"] = "Most_frequent"
            macolonne["encoder"] = "OneHot_Encoder"

            macolonne["nature"] = "categoriel"

        liste_col[col] = macolonne

    return liste_col


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
        id = request.POST.get('id', 0)
        if id == 0:
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
        
        request.session['projet_id'] = id
        return JsonResponse({'data':{'id': id, 'msg':'Information enregistré avec success'}})
    
"""def upload_dataset(request):
    
    ts = time.gmtime()
    ts = time.strftime("__%Y_%m_%d__%H_%M_%S", ts)

    if request.method == 'POST':  
        fichier = request.FILES['file'].read()
        nom_fichier = request.POST['filename'] 
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
                filename =  Fichier.objects.latest('id')

                if old_file_id is not None:
                    #filename = Fichier.objects.get(pk=(old_file_id)
                    filename =  Fichier.objects.latest('id')
                    
                    print("--------->>old_file_idold_file_idold_file_id",filename)
                    media_root = getattr(settings, 'MEDIA_ROOT', None)
                    path_file = os.path.join(media_root, filename)
                    if os.path.isfile(path_file):
                        os.remove(path_file)

                    Fichier.objects.filter(id=old_file_id).delete()
                request.session['fichier_id'] = FileFolder.pk
                
                if int(end):
                    data = info_dataset(path)
                    print("infos dataset",data)
                    res = JsonResponse({'msg':'Chargment effectué avec success','data': data, 'chemin': chemin})
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
                            data = info_dataset(model_id.chemin)
                            res = JsonResponse({'msg':'Chargement effectué avec success','data': data, 'chemin': model_id.chemin})
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
"""

###############################################################################################################

def upload_dataset(request):
    if request.method == 'POST':
        try:
            if(request.POST['file'] == ""):
                context = {'message':"!!! VOUS n'avez pas enté un fichier !!!"}
                return render(request, 'donnees.html',context)
        except Exception as e:
            context = {'message':e}
            print("vous avez entrez un fichier",e)
            #return render(request, 'donnees.html', context)

        myfile = request.FILES['file']
        #header = request.POST['header']

        a_string = "abc"

        extension = [ "csv", "xls", "xlsx"]

        extension_tuple = tuple(extension)

        #ends_with_string = a_string.endswith(extension_tuple)

        if not myfile.name.endswith(extension_tuple):
            context = {'message':"!!! FORMAT DE FICHIER INCORECTE !!!"}
            res = JsonResponse({'data':'FORMAT DE FICHIER INCORECTE !!!'})
            return res

        else:
            fs = FileSystemStorage()

            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            data_upload = source + uploaded_file_url
            dataset = Dataset()
            dataset.source_dataset = data_upload
            dataset.save()

            projet = Projet.objects.latest('id')
            projet.dataset = dataset
            projet.save()

            if myfile.name.endswith(".csv"):
                if header =='noheader':
                    frame = pd.DataFrame(pd.read_csv(data_upload,header=None))
                else:
                    frame = pd.DataFrame(pd.read_csv(data_upload))
            else:
                if header == 'noheader':
                    frame = pd.DataFrame(pd.read_excel(data_upload, header=None,index_col = 0),sep=";")
                else:
                    frame = pd.DataFrame(pd.read_excel(data_upload,header=None,index_col = 0))
                    
                
            dataframe = frame

            print("---------------------",frame)
           
            res = JsonResponse({'msg':'Chargement effectué avec success','data': data, 'chemin': 'model_id.chemin'})
    else:
        res = JsonResponse({'data':'Requete non authorisée'})
        return res



       


###############################################################################################################


#FONCTION EXTRACTION DES CARACTERISQUE D'UNE COLONNE
def infos_dataset(dataframe):

    columns = dataframe.columns
    liste_col = {}
    for col in columns:
        macolonne = {}
        macolonne["type"] = dataframe[col].dtype
        macolonne["data"] = list(dataframe[col])

        if (dataframe[col].dtype == "int64" or dataframe[col].dtype == "int32"):
            macolonne["scaler"] = "Standard_Scaler"
            macolonne["imputer"] = "Mean"
            macolonne["encoder"] = "None"
            if dataframe[col].count() < 10:
                macolonne["nature"] = "discret"
            else:
                macolonne["nature"] = "continue"

        elif (dataframe[col].dtype == "bool"):
            macolonne["scaler"] = "None"
            macolonne["imputer"] = "Most_frequent"
            macolonne["encoder"] = "OneHot_Encoder"

            macolonne["nature"] = "discret"
        else:
            macolonne["scaler"] = "None"
            macolonne["imputer"] = "Most_frequent"
            macolonne["encoder"] = "OneHot_Encoder"

            macolonne["nature"] = "categoriel"

        liste_col[col] = macolonne

    return liste_col


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