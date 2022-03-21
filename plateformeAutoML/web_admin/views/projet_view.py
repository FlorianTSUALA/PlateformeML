from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import JsonResponse
from django.http import JsonResponse

from web_admin.models import Algorithme
import pandas as pd
from web_admin.models import Fichier
# Create your views here.

ALLOWED_EXTENSIONS = set(["npy", "csv", "xls", "xlsx"])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def clean_session_project_creation(request):
    pass
from .models import File

def index(request):
    if request.method == 'POST':  
        file = request.FILES['file'].read()
        fileName= request.POST['filename']
        existingPath = request.POST['existingPath']
        end = request.POST['end']
        nextSlice = request.POST['nextSlice']

        if file=="" or fileName=="" or existingPath=="" or end=="" or nextSlice=="":
            res = JsonResponse({'data':'Invalid Request'})
            return res
        else:
            if existingPath == 'null':
                path = 'media/' + fileName
                with open(path, 'wb+') as destination: 
                    destination.write(file)
                FileFolder = File()
                FileFolder.existingPath = fileName
                FileFolder.eof = end
                FileFolder.name = fileName
                FileFolder.save()
                if int(end):
                    res = JsonResponse({'data':'Uploaded Successfully','existingPath': fileName})
                else:
                    res = JsonResponse({'existingPath': fileName})
                return res

            else:
                path = 'media/' + existingPath
                model_id = File.objects.get(existingPath=existingPath)
                if model_id.name == fileName:
                    if not model_id.eof:
                        with open(path, 'ab+') as destination: 
                            destination.write(file)
                        if int(end):
                            model_id.eof = int(end)
                            model_id.save()
                            res = JsonResponse({'data':'Uploaded Successfully','existingPath':model_id.existingPath})
                        else:
                            res = JsonResponse({'existingPath':model_id.existingPath})    
                        return res
                    else:
                        res = JsonResponse({'data':'EOF found. Invalid request'})
                        return res
                else:
                    res = JsonResponse({'data':'No such file exists in the existingPath'})
                    return res
    return render(request, 'index.html')

    
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
    
def file_upload(request):
    
    # if request.method == 'POST':
    #     values = {}
    #     # check if the post request has the file part
    #     if 'file' not in request.files:
    #         flash('No file part')
    #         return redirect(request.url)
    #     file = request.files['file']
    #     #data_type = request.form['data_type']
    #     data_type = "csv"
    #     task = request.form['task']
    #     sep = request.form['sep']
    #     #sep= None
    #     if file.filename == '':
    #         flash('No file selected for uploading')
    #         return redirect(request.url)
    #     if file :
    #         filename = secure_filename(file.filename)
    #         if data_type == "numpy" and filename[-3:] != "npy":
    #             return "Wrong file extension (expected .npy)"
    #         if data_type == "csv" and (filename[-3:] != "csv" and filename[-3:] != "CSV"):
    #             err = "Unsupported file extension (expected .csv)"
    #             return render_template("error.html", err=err)
    #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #         values['task'] = task
    #         values["sep"] = sep
    #         session["filename"] = filename
    #         session["values"] = values
    #         session["data_type"] = data_type
    #         session["task"] = task
    #         return redirect(url_mod("featur_pg"))
    #     else:
    #         flash('Allowed file types are: {}'.format(str(ALLOWED_EXTENSIONS)))
    #         return redirect(request.url)

    if request.method == 'POST':  
        fichier = request.FILES['fichier'].read()
        nom_fichier= request.POST['nom_fichier']
        chemin = request.POST['chemin']
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
                FileFolder = File()
                FileFolder.chemin = nom_fichier
                FileFolder.eof = end
                FileFolder.name = nom_fichier
                FileFolder.save()
                if int(end):
                    res = JsonResponse({'data':'Chargment effectué avec success','chemin': nom_fichier})
                else:
                    res = JsonResponse({'chemin': nom_fichier})
                return res

            else:
                path = 'media/' + chemin
                model_id = File.objects.get(chemin=chemin)
                if model_id.name == nom_fichier:
                    if not model_id.eof:
                        with open(path, 'ab+') as destination: 
                            destination.write(fichier)
                        if int(end):
                            model_id.eof = int(end)
                            model_id.save()
                            res = JsonResponse({'data':'Uploaded Successfully','chemin':model_id.chemin})
                        else:
                            res = JsonResponse({'chemin':model_id.chemin})    
                        return res
                    else:
                        res = JsonResponse({'data':'EOF found. Invalid request'})
                        return res
                else:
                    res = JsonResponse({'data':'No such fichier exists in the chemin'})
                    return res
    return render(request, 'index.html')

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