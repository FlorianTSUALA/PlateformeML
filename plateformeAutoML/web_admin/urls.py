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
# from .views import ProjetListView, ProjetDetailView
from web_admin.views import (
    #Authentification
    login,


    #Accueil
    VitrineView,
    AccueilView, 
    MesFavorisView, 
    MesProjetsView, 
    ProjetsPublicsView, 
    NouveauProjetView, 
    ConsulterProjetView, 
    ModifierProjetView, 
    ListeProjetView, 

    tache,
    tache_create,
    tache_update,
    tache_delete,

    AlgorithmeView, 
    # ProjetListView, 

    #Autres
    FAQView, 
    AProposView, 
    
    
    #Utilisateurs
    MonCompteView, 
    ListUtilisateurView, 
    CreateUtilisateurView,


    #FAMILLE
    ListFamilleView,
    CreateFamilleView,
    UpdateFamilleView,
    DeleteFamilleView,

    #ALGORITHME
    ListalgorithmeView,
    CreateAlgorithmeView,
    UpdateAlgorithmeView,
    DeleteAlgorithmeView,
)

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('parametre/algorithmes/', views.AlgorithmeListView.as_view(), name='algorithmes'),
#     path('parametre/algorithme/<int:pk>', views.AlgorithmeDetailView.as_view(), name='algorithme-detail'),
# ]

urlpatterns = [
    #Authentification
    path('login',  VitrineView.as_view(), name='vitrine'),



    #Vitrine
    path('presentation',  VitrineView.as_view(), name='vitrine'),

    #Accueil
    path('',  AccueilView.as_view(), name='accueil'),
    path('mes-favoris',  MesFavorisView.as_view(), name='mes_favoris'),
    path('mes-projets',  MesProjetsView.as_view(), name='mes_projets'),
    path('projets-publics',  ProjetsPublicsView.as_view(), name='projets_publics'),
    path('nouveau-projet',  NouveauProjetView.as_view(), name='nouveau_projet'),
    path('consulter-projet',  ConsulterProjetView.as_view(), name='consulter_projet'),
    path('modifier-projet',  ModifierProjetView.as_view(), name='modifier_projet'),
    path('liste-projet/<str:filter>',  ListeProjetView.as_view(), name='liste_projet'),
    #Autres
    path('faq',  FAQView.as_view(), name='faq'),
    path('a-propos',  AProposView.as_view(), name='apropos'),

    #Utilisateurs
    path('utilisateur/mon-compte',  MonCompteView.as_view(), name='mon_compte'),
    path('utilisateur/list',  ListUtilisateurView.as_view(), name='utilisateur_list'),
    path('utilisateur/list/archives',  ListUtilisateurView.as_view(), name='utilisateur_list_archives'),
    path('utilisateur/list/attente_validation',  ListUtilisateurView.as_view(), name='utilisateur_list_attente_validation'),
    path('utilisateur/create',  CreateUtilisateurView.as_view(), name='utilisateur_create'),

    #Paramtrage
    # path('projet/',  ProjetListView.as_view(), name='projet'),
    path('parametrage/algorithme',  AlgorithmeView.as_view(), name='algorithme'),
    path('template/',  AlgorithmeView.as_view(), name='template'),
    path('default/',  AlgorithmeView.as_view(), name='default'),
    
    # #famille
    # path('parametrage/famille',  ListFamilleView.as_view(), name='famille_list'),
    # path('parametrage/famille/create/',  CreateFamilleView.as_view(), name='famille_create'),
    # path('parametrage/famille/update/',  UpdateFamilleView.as_view(), name='famille_update'),
    # path('parametrage/famille/delete/',  DeleteFamilleView.as_view(), name='famille_delete'),

    # #algorithme
    path('parametrage/algorithme',  ListalgorithmeView.as_view(), name='algorithme'),
    path('parametrage/algorithme/create/',  CreateAlgorithmeView.as_view(), name='algorithme_create'),
    path('parametrage/algorithme/update/',  UpdateAlgorithmeView.as_view(), name='algorithme_update'),
    path('parametrage/algorithme/delete/',  DeleteAlgorithmeView.as_view(), name='algorithme_delete'),
    #Metrique
    path('parametrage/metrique',  ListFamilleView.as_view(), name='metrique'),
    path('parametrage/metrique/create/',  CreateFamilleView.as_view(), name='metrique_create'),
    path('parametrage/metrique/update/',  UpdateFamilleView.as_view(), name='metrique_update'),
    path('parametrage/metrique/delete/',  DeleteFamilleView.as_view(), name='metrique_delete'),
    #CritereCompraison
    path('parametrage/critere_compraison',  ListFamilleView.as_view(), name='critere_comparaison'),
    path('parametrage/critere_compraison/create/',  CreateFamilleView.as_view(), name='critere_comparaison_create'),
    path('parametrage/critere_compraison/update/',  UpdateFamilleView.as_view(), name='critere_comparaison_update'),
    path('parametrage/critere_compraison/delete/',  DeleteFamilleView.as_view(), name='critere_comparaison_delete'),
    #Package Alogorithme
    path('parametrage/package_algorithme',  ListFamilleView.as_view(), name='package_algorithme'),
    path('parametrage/package_algorithme/create/',  CreateFamilleView.as_view(), name='package_algorithme_create'),
    path('parametrage/package_algorithme/update/',  UpdateFamilleView.as_view(), name='package_algorithme_update'),
    path('parametrage/package_algorithme/delete/',  DeleteFamilleView.as_view(), name='package_algorithme_delete'),
    #FAMILLE
    path('parametrage/famille_algorithme',  ListFamilleView.as_view(), name='famille_algorithme'),
    path('parametrage/famille_algorithme/create/',  CreateFamilleView.as_view(), name='famille_algorithme_create'),
    path('parametrage/famille_algorithme/update/',  UpdateFamilleView.as_view(), name='famille_algorithme_update'),
    path('parametrage/famille_algorithme/delete/',  DeleteFamilleView.as_view(), name='famille_algorithme_delete'),
    #Tache ML
    # path('parametrage/tache', tache, name='tache'),
    path('parametrage/tache/',  tache, name='tache'),
    path('parametrage/tache/create/',  tache_create, name='tache_create'),
    path('parametrage/tache/<int:pk>/update/',  tache_update, name='tache_update'),
    path('parametrage/tache/<int:pk>/delete/',  tache_delete, name='tache_delete'),

    # path('parametrage/tache/create/',  CreateFamilleView.as_view(), name='tache_create'),
    # path('parametrage/tache/update/',  UpdateFamilleView.as_view(), name='tache_update'),
    # path('parametrage/tache/delete/',  DeleteFamilleView.as_view(), name='tache_delete'),
    #Type Apprentissage
    path('parametrage/type_apprentissage',  ListFamilleView.as_view(), name='type_apprentissage'),
    path('parametrage/type_apprentissage/create/',  CreateFamilleView.as_view(), name='type_apprentissage_create'),
    path('parametrage/type_apprentissage/update/',  UpdateFamilleView.as_view(), name='type_apprentissage_update'),
    path('parametrage/type_apprentissage/delete/',  DeleteFamilleView.as_view(), name='type_apprentissage_delete'),
    #Taxonomie Type Données
    path('parametrage/taxonomie_type_donnee',  ListFamilleView.as_view(), name='taxonomie_type_donnee'),
    path('parametrage/taxonomie_type_donnee/create/',  CreateFamilleView.as_view(), name='taxonomie_type_donnee_create'),
    path('parametrage/taxonomie_type_donnee/update/',  UpdateFamilleView.as_view(), name='taxonomie_type_donnee_update'),
    path('parametrage/taxonomie_type_donnee/delete/',  DeleteFamilleView.as_view(), name='taxonomie_type_donnee_delete'),
    #Valeurs Manquante
    path('parametrage/valeur_manquante',  ListFamilleView.as_view(), name='valeur_manquante'),
    path('parametrage/valeur_manquante/create/',  CreateFamilleView.as_view(), name='valeur_manquante_create'),
    path('parametrage/valeur_manquante/update/',  UpdateFamilleView.as_view(), name='valeur_manquante_update'),
    path('parametrage/valeur_manquante/delete/',  DeleteFamilleView.as_view(), name='valeur_manquante_delete'),
    #Encodage
    path('parametrage/encodage',  ListFamilleView.as_view(), name='encodage'),
    path('parametrage/encodage/create/',  CreateFamilleView.as_view(), name='encodage_create'),
    path('parametrage/encodage/update/',  UpdateFamilleView.as_view(), name='encodage_update'),
    path('parametrage/encodage/delete/',  DeleteFamilleView.as_view(), name='encodage_delete'),
    #Mise Echelle
    path('parametrage/mise_echelle',  ListFamilleView.as_view(), name='mise_echelle'),
    path('parametrage/mise_echelle/create/',  CreateFamilleView.as_view(), name='mise_echelle_create'),
    path('parametrage/mise_echelle/update/',  UpdateFamilleView.as_view(), name='mise_echelle_update'),
    path('parametrage/mise_echelle/delete/',  DeleteFamilleView.as_view(), name='mise_echelle_delete'),
]