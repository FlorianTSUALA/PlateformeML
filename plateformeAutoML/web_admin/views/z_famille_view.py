from django.shortcuts import render
from django.urls import reverse_lazy
from web_admin.models import Famille
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import JsonResponse


# class FamilleListView(ListView):
#     model = Famille
#     template_name = 'parametrage/famille.html'  # Default: <app_label>/<model_name>_list.html
#     context_object_name = 'familles'  # Default: object_list
#     paginate_by = 10
#     queryset = Famille.objects.all()  # Default: Model.objects.all()


class ListFamilleView(ListView):
    model = Famille
    template_name = 'pages/parametrage/famille.html'
    context_object_name = 'items'
    paginate_by = 10
	# ordering = ['-created']

    def get_queryset(self):
        return Book.objects.filter(created_by=self.request.user)

    def get_queryset(self):
        query = self.request.GET.get('q')
        return model.objects.filter(title=q)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_title'] = 'Parametrage'
        context['section_item_title'] = 'Famille'
        return context

    def get_queryset(self):
        return Book.objects.filter(created_by=self.request.user)

class CreateFamilleView(View):
    def  get(self, request):
        libelle = request.GET.get('libelle', None)
        description = request.GET.get('description', None)
        age1 = request.GET.get('age', None)

        obj = Famille.objects.create(
            name = libelle,
            address = description,
            age = age1
        )

        data = Famille.objects.all()

        data = {
            'data': data
        }
        return JsonResponse(data)

class DeleteFamilleView(View):
    def  get(self, request):
        id = request.GET.get('id', None)
        Famille.objects.get(id=id).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateFamilleView(View):
    def  get(self, request):
        id = request.GET.get('id', None)
        libelle = request.GET.get('name', None)
        description = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = Famille.objects.get(id=id)
        obj.name = libelle
        obj.address = description
        obj.age = age1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class IncidentEdit(UpdateView):

    def form_valid(self, form):
        if form.cleaned_data['email'] in \
        [i.email for i in Incident.objects.exclude(id=get_object().id)]:
            # Assume incident have email and it should be unique !!
            form.add_error('email', 'Incident with this email already exist')
            return self.form_invalid(form)
        return super(IncidentEdit, self).form_valid(form)