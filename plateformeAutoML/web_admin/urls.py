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
from web_admin.views import (
    #Authentification
    login,
    logout,
    register,


    #Accueil
    VitrineView,
    AccueilView, 
    MesFavorisView, 
    MesProjetsView, 
    ProjetsPublicsView, 
    
    NouveauProjetView, 
    save_info_projet,
    # upload_dataset,
    # clean_session_project_creation,

    ConsulterProjetView, 
    ModifierProjetView, 
    ListeProjetView, 


    # ProjetListView, 

    #AUTRES
    FAQView, 
    AProposView, 
    
    
    #Utilisateurs
    MonCompteView, 
    ListUtilisateurView, 
    CreateUtilisateurView,


    #ALGORITHME
    algorithme,
    algorithme_create,
    algorithme_update,
    algorithme_delete,

    #CRITERE_COMPARAISON
    critere_comparaison,
    critere_comparaison_create,
    critere_comparaison_update,
    critere_comparaison_delete,

    #FAMILLE
    famille,
    famille_create,
    famille_update,
    famille_delete,

    #PACKAGE
    package,
    package_create,
    package_update,
    package_delete,

    #TACHE
    tache,
    tache_create,
    tache_update,
    tache_delete,

    #TAXONOMIE TYPE DE DONNES
    taxonomie_type_donnee, 
    taxonomie_type_donnee_create,  
    taxonomie_type_donnee_update,  
    taxonomie_type_donnee_delete,

    #TYPE APPRENTISSAGE
    type_apprentissage, 
    type_apprentissage_create,  
    type_apprentissage_update,  
    type_apprentissage_delete,

)

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('parametre/algorithmes/', views.AlgorithmeListView.as_view(), name='algorithmes'),
#     path('parametre/algorithme/<int:pk>', views.AlgorithmeDetailView.as_view(), name='algorithme-detail'),
# ]

urlpatterns = [
    #Authentification
    path('login',  login, name='login'),
    path('register',  register, name='register'),

    #Vitrine
    path('presentation',  VitrineView.as_view(), name='vitrine'),

    #Accueil
    path('',  AccueilView.as_view(), name='home'),
    path('',  AccueilView.as_view(), name='accueil'),
    path('mes-favoris',  MesFavorisView.as_view(), name='mes_favoris'),
    path('mes-projets',  MesProjetsView.as_view(), name='mes_projets'),
    path('projets-publics',  ProjetsPublicsView.as_view(), name='projets_publics'),
    
    path('nouveau-projet',  NouveauProjetView.as_view(), name='nouveau_projet'),
    # path('clean_session_project_creation',  clean_session_project_creation, name='clean_session_project_creation'),
    # path('upload_dataset',  upload_dataset, name='upload_dataset'),
    
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
    
    # #famille
    # path('parametrage/famille',  famille, name='famille_list'),
    # path('parametrage/famille/create/',  famille_create, name='famille_create'),
    # path('parametrage/famille/update/',  famille_update, name='famille_update'),
    # path('parametrage/famille/delete/',  famille_delete, name='famille_delete'),

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

    #Valeurs Manquante
    path('parametrage/valeur_manquante',  famille, name='valeur_manquante'),
    path('parametrage/valeur_manquante/create/',  famille_create, name='valeur_manquante_create'),
    path('parametrage/valeur_manquante/<int:pk>/update/',  famille_update, name='valeur_manquante_update'),
    path('parametrage/valeur_manquante/<int:pk>/delete/',  famille_delete, name='valeur_manquante_delete'),
    #Encodage
    path('parametrage/encodage',  famille, name='encodage'),
    path('parametrage/encodage/create/',  famille_create, name='encodage_create'),
    path('parametrage/encodage/<int:pk>/update/',  famille_update, name='encodage_update'),
    path('parametrage/encodage/<int:pk>/delete/',  famille_delete, name='encodage_delete'),
    #Mise Echelle
    path('parametrage/mise_echelle',  famille, name='mise_echelle'),
    path('parametrage/mise_echelle/create/',  famille_create, name='mise_echelle_create'),
    path('parametrage/mise_echelle/<int:pk>/update/',  famille_update, name='mise_echelle_update'),
    path('parametrage/mise_echelle/<int:pk>/delete/',  famille_delete, name='mise_echelle_delete'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)