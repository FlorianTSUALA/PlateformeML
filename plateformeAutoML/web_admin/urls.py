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
    AlgorithmeView, 
    ProjetListView, 
    AccueilView, 
    #FAMILLE
    ListFamilleView,
    CreateFamilleView,
    UpdateFamilleView,
    DeleteFamilleView,
)

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('parametre/algorithmes/', views.AlgorithmeListView.as_view(), name='algorithmes'),
#     path('parametre/algorithme/<int:pk>', views.AlgorithmeDetailView.as_view(), name='algorithme-detail'),
# ]

urlpatterns = [
    path('',  AccueilView.as_view(), name='accueil'),
    path('projet/',  ProjetListView.as_view(), name='projet'),
    path('parametrage/algorithme',  AlgorithmeView.as_view(), name='algorithme'),
    path('template/',  AlgorithmeView.as_view(), name='template'),
    path('default/',  AlgorithmeView.as_view(), name='default'),
    
    #FAMILLE
    path('parametrage/famille',  ListFamilleView.as_view(), name='famille_list'),
    path('parametrage/famille/create/',  CreateFamilleView.as_view(), name='famille_create'),
    path('parametrage/famille/update/',  UpdateFamilleView.as_view(), name='famille_update'),
    path('parametrage/famille/delete/',  DeleteFamilleView.as_view(), name='famille_delete'),
]

# urlpatterns2 = [
#     # path('<int:pk>', ProjetDetailView.as_view(), name='projet_detail'),
#     # path('', ProjetListView.as_view(), name='projet_list'),
# ]

# urlpatterns += urlpatterns2
