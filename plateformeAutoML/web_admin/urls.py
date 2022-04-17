"""Compagnie_aerienne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from web_admin.views import (
    #AUTHENTIFICATION
    connexion, deconnexion, inscription, 
    #PROFILE = COMPTE + UTILISATEUR
    profile, profile_list,  profile_create, profile_update, profile_delete,
    #ACCUEIL
    VitrineView,
    #PROJET
    AccueilView, MesFavorisView, MesProjetsView, ProjetsPublicsView, NouveauProjetView, 
    ConsulterProjetView, ModifierProjetView, ListeProjetView, 
    save_projet_info, upload_dataset, clean_session_projet_creation, save_preprocessing, 
    save_selection_variable, save_selection_algorithme, get_algorithme_by_task, 
    #AUTRES
    FAQView, AProposView, 
    #ALGORITHME
    algorithme, algorithme_create, algorithme_update, algorithme_delete,
    #CRITERE_COMPARAISON
    critere_comparaison, critere_comparaison_create, critere_comparaison_update, critere_comparaison_delete, 
    #FAMILLE
    famille, famille_create, famille_update, famille_delete,
    #PACKAGE
    package, package_create, package_update, package_delete,
    #TACHE
    tache, tache_create, tache_update, tache_delete,
    #TAXONOMIE TYPE DE DONNES
    taxonomie_type_donnee, taxonomie_type_donnee_create, taxonomie_type_donnee_update, taxonomie_type_donnee_delete,
    #TYPE APPRENTISSAGE
    type_apprentissage, type_apprentissage_create, type_apprentissage_update, type_apprentissage_delete,
    #STATEGIE PRETRAITEMENT
    strategie_pretraitement, strategie_pretraitement_update,
    encodage, encodage_update, imputation, imputation_update, mise_echelle, mise_echelle_update,
    strategie_encodage, strategie_encodage_update, strategie_imputation, strategie_imputation_update, strategie_mise_echelle, strategie_mise_echelle_update,
    #INITIALISATION
    initialisation,
)

urlpatterns = [
    #Authentification
    path('connexion',  connexion, name='connexion'),
    path('inscription',  inscription, name='inscription'),
    path('deconnexion',  deconnexion, name='deconnexion'),

    #Vitrine
    path('presentation',  VitrineView.as_view(), name='vitrine'),

    #Accueil
    path('',  AccueilView.as_view(), name='home'),
    path('',  AccueilView.as_view(), name='accueil'),

    ####################################################################################################################################
    #####################   DYNAMAIQUE
    ####################################################################################################################################

    #####################   CONSULTATION
    
    path('mes-favoris',  MesFavorisView.as_view(), name='mes_favoris'),
    path('mes-projets',  MesProjetsView.as_view(), name='mes_projets'),
    path('projets-publics',  ProjetsPublicsView.as_view(), name='projets_publics'),
    

    
    #####################   CREATION

    path('nouveau-projet',  login_required(NouveauProjetView.as_view()), name='nouveau_projet'),
    path('clean_session/projet_creation',  clean_session_projet_creation, name='clean_session_projet_creation'),
    path('upload_dataset',  upload_dataset, name='upload_dataset'),
    path('save_projet_info',  save_projet_info, name='save_projet_info'),
    path('save_preprocessing',  save_preprocessing, name='save_preprocessing'),
    path('save_selection_variable',  save_selection_variable, name='save_selection_variable'),
    path('save_selection_algorithme',  save_selection_algorithme, name='save_selection_algorithme'),
    path('get_algorithme_by_task',  get_algorithme_by_task, name='get_algorithme_by_task'),
    
    path('consulter-projet',  ConsulterProjetView.as_view(), name='consulter_projet'),
    path('modifier-projet',  ModifierProjetView.as_view(), name='modifier_projet'),
    path('liste-projet/<str:filter>',  ListeProjetView.as_view(), name='liste_projet'),


    ####################################################################################################################################
    #####################   AUTRES
    ####################################################################################################################################

    path('faq',  FAQView.as_view(), name='faq'),
    path('a-propos',  AProposView.as_view(), name='apropos'),


    ####################################################################################################################################
    #####################   PROFILE = COMPTE + UTILISATEUR
    ####################################################################################################################################
    
    path('profile/list/<str:filter>', profile_list, name='profile_list'),
    #TODO Archive, Validation : post
    # path('profile/list/archives',  ProfileListView.as_view(), name='profile_list_archives'),
    # path('profile/list/attente_validation',  ProfileListView.as_view(), name='profile_list_attente_validation'),
    
    path('profile',  profile, name='profile'),
    # path('profile/create',  profile_create, name='profile_create'),
    path('profile/update', profile_update, name='profile_update'),
    path('profile/delete/<int:pk>', profile_delete, name='profile_delete'),

    #Paramtrage
        ####################################################################################################################################
        #####################   DYNAMAIQUE
        ####################################################################################################################################

            ####################################################################################################################################
            #####################   STRATEGIE : IMPUATION, MORMALISATIOIN, ENCODAGE
            ####################################################################################################################################
            path('parametrage/stategie/pretraitement',  strategie_pretraitement, name='strategie_pretraitement'),
            path('parametrage/stategie/pretraitement/<int:pk>/update/',  strategie_pretraitement_update, name='strategie_pretraitement_update'),
           
            path('parametrage/stategie/encodage',  strategie_encodage, name='strategie_encodage'),
            path('parametrage/stategie/encodage/<int:pk>/update/',  strategie_encodage_update, name='strategie_encodage_update'),
            path('parametrage/stategie/mise_echelle',  strategie_mise_echelle, name='strategie_mise_echelle'),
            path('parametrage/stategie/mise_echelle/<int:pk>/update/',  strategie_mise_echelle_update, name='strategie_mise_echelle_update'),
            path('parametrage/stategie/imputation',  strategie_imputation, name='strategie_imputation'),
            path('parametrage/stategie/imputation/<int:pk>/update/',  strategie_imputation_update, name='strategie_imputation_update'),
           
            path('parametrage/encodage',  encodage, name='encodage'),
            path('parametrage/encodage/<int:pk>/update/',  encodage_update, name='encodage_update'),
            path('parametrage/mise_echelle',  mise_echelle, name='mise_echelle'),
            path('parametrage/mise_echelle/<int:pk>/update/',  mise_echelle_update, name='mise_echelle_update'),
            path('parametrage/imputation',  imputation, name='imputation'),
            path('parametrage/imputation/<int:pk>/update/',  imputation_update, name='imputation_update'),
        
            #INITIALISATION
            path('parametrage/initialisation',  initialisation, name='initialisation'),


        ####################################################################################################################################
        #####################   DYNAMAIQUE
        ####################################################################################################################################
    # #algorithme
    path('parametrage/algorithme',  algorithme, name='algorithme'),
    path('parametrage/algorithme/create/',  algorithme_create, name='algorithme_create'),
    path('parametrage/algorithme/<int:pk>/update/',  algorithme_update, name='algorithme_update'),
    path('parametrage/algorithme/<int:pk>/delete/',  algorithme_delete, name='algorithme_delete'),

    #Metrique
    path('parametrage/metrique',  famille, name='metrique'),
    path('parametrage/metrique/create/',  famille_create, name='metrique_create'),
    path('parametrage/metrique/<int:pk>/update/',  famille_update, name='metrique_update'),
    path('parametrage/metrique/<int:pk>/delete/',  famille_delete, name='metrique_delete'),

    #CritereCompraison
    path('parametrage/critere_comparaison/',  critere_comparaison, name='critere_comparaison'),
    path('parametrage/critere_comparaison/create/',  critere_comparaison_create, name='critere_comparaison_create'),
    path('parametrage/critere_comparaison/<int:pk>/update/',  critere_comparaison_update, name='critere_comparaison_update'),
    path('parametrage/critere_comparaison/<int:pk>/delete/',  critere_comparaison_delete, name='critere_comparaison_delete'),

    #Package Alogorithme
    path('parametrage/package/',  package, name='package'),
    path('parametrage/package/create/',  package_create, name='package_create'),
    path('parametrage/package/<int:pk>/update/',  package_update, name='package_update'),
    path('parametrage/package/<int:pk>/delete/',  package_delete, name='package_delete'),

    #FAMILLE
    path('parametrage/famille/',  famille, name='famille'),
    path('parametrage/famille/create/',  famille_create, name='famille_create'),
    path('parametrage/famille/<int:pk>/update/',  famille_update, name='famille_update'),
    path('parametrage/famille/<int:pk>/delete/',  famille_delete, name='famille_delete'),

    #Tache ML
    path('parametrage/tache/',  tache, name='tache'),
    path('parametrage/tache/create/',  tache_create, name='tache_create'),
    path('parametrage/tache/<int:pk>/update/',  tache_update, name='tache_update'),
    path('parametrage/tache/<int:pk>/delete/',  tache_delete, name='tache_delete'),

    #Type Apprentissage
    path('parametrage/type_apprentissage/',  type_apprentissage, name='type_apprentissage'),
    path('parametrage/type_apprentissage/create/',  type_apprentissage_create, name='type_apprentissage_create'),
    path('parametrage/type_apprentissage/<int:pk>/update/',  type_apprentissage_update, name='type_apprentissage_update'),
    path('parametrage/type_apprentissage/<int:pk>/delete/',  type_apprentissage_delete, name='type_apprentissage_delete'),

    #Taxonomie Type Données
    path('parametrage/taxonomie_type_donnee/',  taxonomie_type_donnee, name='taxonomie_type_donnee'),
    path('parametrage/taxonomie_type_donnee/create/',  taxonomie_type_donnee_create, name='taxonomie_type_donnee_create'),
    path('parametrage/taxonomie_type_donnee/<int:pk>/update/',  taxonomie_type_donnee_update, name='taxonomie_type_donnee_update'),
    path('parametrage/taxonomie_type_donnee/<int:pk>/delete/',  taxonomie_type_donnee_delete, name='taxonomie_type_donnee_delete'),
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)