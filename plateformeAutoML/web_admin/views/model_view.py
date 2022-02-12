from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView 
from django.contrib.auth.decorators import login_required, permission_required 
#@permission_required('polls.add_choice', raise_exception=True)
#https://docs.djangoproject.com/en/3.2/topics/auth/default/#the-permissionrequiredmixin-mixin
from django.views.decorators.http import require_http_methods
from django.views.generic import FormView, TemplateView
from access_control.models import Model

def model_metadata(key = None): 

    model = 'model'
    data = {
        'model': model,
        'genre': 'F',
        'url_create': model + '_create',
        'url_update': model + '_update',
        'url_delete': model + '_delete',
        'path_script': 'custom/js/entity.js',
        'path_table_body': 'partials/entity/table_body.html',
        'path_form_update': 'partials/entity/form_update.html',
        'path_form_create': 'partials/entity/form_create.html',
        'path_form_delete': 'partials/entity/form_delete.html',
    }
    genre = 'M'
    data['title_modal_create'] = 'Creer ' +  ('une nouvelle', 'un nouveau')[ genre == 'F']  + f' {model}'

    if key is None:
        return data
    return data.get(key, '')

class ModelIndexView(TemplateView):
    template_name = 'model.html'

# class Login(LoginView):
#     template_name = 'registration/login.html'

class ModelList(LoginRequiredMixin, ListView):
    template_name = 'model.html'
    model = Model
    context_object_name = 'models'

    def get_queryset(self):
        compte = self.request.compte
        return compte.models.all()


def search_model(request):
    search_text = request.POST.get('search')
    results = Model.objects.filter(name__icontains=search_text)
    context = {'results': results}
    return render(request, 'partials/model/search-results.html', context)

@login_required
def home_model(request):
    name = request.GET.get('name')
    model = Model.objects.create(name=name)

    # request.user.model.add(model)
    models = Model.objects.all()
    return render(request, 'partials/model/list.html',{models: models})

@login_required
@require_http_methods(['POST'])
def add_model(request):
    label = request.POST.get('label')
    description = request.POST.get('description')
    statut = request.POST.get('statut', None)
    if statut is None:
        statut = False
    else:
        statut = True

    # add model
    model = Model.objects.create(label=label, description=description, statut=statut)

    # add the model to the user's list
    request.user.models.add(model)

    # return template fragment with all the user's models
    models = Model.objects.all()
    return render(request, 'partials/model/list.html',{models: models})


def check_libelle(request):
    print('Request check Model Label')
    label = request.POST.get('label', None)
    if Model.objects.filter(label=label).exists():
        return HttpResponse("This label already exists")
    else:
        return HttpResponse("")

def update_model(request):
    name = request.GET.get('name')
    model = Model.objects.create(name=name)

    # request.user.model.add(model)
    models = Model.objects.all()
    return render(request, 'partials/model/list.html',{models: models})

@login_required
@require_http_methods(['DELETE'])
def delete_model(request, pk):
    request.user.models.remove(pk)

    models = Model.objects.all()
    return render(request, 'partials/model/list.html',{models: models})


