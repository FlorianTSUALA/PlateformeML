from django.views.generic import ListView, DetailView

from web_admin.models import Projet

class ProjetListView(ListView):
    model = Projet
    template_name = 'Projet_list.html'


class ProjetDetailView(DetailView):
    model = Projet
    template_name = 'Projet_detail.html'