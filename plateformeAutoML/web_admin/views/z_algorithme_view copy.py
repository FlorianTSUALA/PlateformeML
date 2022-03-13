from django.shortcuts import render
from django.urls import reverse_lazy
from web_admin.models import Algorithme
from django.views.generic import TemplateView, View, DeleteView, ListView, UpdateView
from django.core import serializers
from django.http import JsonResponse

class AlgorithmeListView(ListView):
    model = Algorithme
    template_name = 'algorithme/index.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'algorithmes'  # Default: object_list
    paginate_by = 10
    queryset = Algorithme.objects.all()  # Default: Model.objects.all()


class AlgorithmeView(TemplateView):
    template_name = 'model_template_1.html'
    # template_name = 'algorithme/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section_title'] = 'Parametrage'
        context['section_item_title'] = 'Algorithme'
        return context


class CreateAlgorithmeView(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = Algorithme.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteAlgorithmeView(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Algorithme.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateAlgorithmeView(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = Algorithme.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
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