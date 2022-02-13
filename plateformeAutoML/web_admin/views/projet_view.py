from django.views.generic import ListView, DetailView

from .models import Projet

class ProjetListView(ListView):
    model = Projet
    template_name = 'Projet_list.html'


class ProjetDetailView(DetailView):
    model = Projet
    template_name = 'Projet_detail.html'