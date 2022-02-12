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
from web_admin.views import (

    model_create, 
    model_update, 
    model_delete, 
    model,

)



urlpatterns = [
    #account access

    path('project/',  project, name='project'),
    path('project/project_create/',  project_create, name='project_create'),
    path('project/<int:pk>/update/',  project_update, name='project_update'),
    path('project/<int:pk>/delete/',  project_delete, name='admin_delete'),

    path('login/',  user_login, name='login'),

]