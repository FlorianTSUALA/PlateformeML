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
)

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('parametre/algorithmes/', views.AlgorithmeListView.as_view(), name='algorithmes'),
#     path('parametre/algorithme/<int:pk>', views.AlgorithmeDetailView.as_view(), name='algorithme-detail'),
# ]

urlpatterns = [
    path('parametrage/',  AlgorithmeView.as_view(), name='algorithme'),
    # path('parametrage/algorithme/create/',  views.CreateAlgorithmeView.as_view(), name='algorithme_create'),
    # path('parametrage/algorithme/update/',  views.UpdateAlgorithmeView.as_view(), name='algorithme_update'),
    # path('parametrage/algorithme/delete/',  views.DeleteAlgorithmeView.as_view(), name='algorithme_delete'),
]

# urlpatterns2 = [
#     # path('<int:pk>', ProjetDetailView.as_view(), name='projet_detail'),
#     # path('', ProjetListView.as_view(), name='projet_list'),
# ]

# urlpatterns += urlpatterns2
