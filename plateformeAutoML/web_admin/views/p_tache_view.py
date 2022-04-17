from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from web_admin.models import Tache
from web_admin.forms import TacheForm
# Create your views here.

def get_metadata(key = None):

    model = 'tache'
    genre = 'F'

    data = {
        'can_init': True,
        'can_add': True,
        'can_edit': True,
        'can_delete': True,

        'page_title': 'AutoML - Plateforme de Machine Learning Automaisé',
        'table_title': 'Liste des taches du Machine Learning',
        'section_title': 'Parametrage',
        'section_item_title': 'Taches du Machine Learning',
     
        'title_modal_create': f'Creer {("une nouvelle", "un nouveau")[ genre == "F"]} {model}',
     
        'model': model,
        'genre': 'F',

        'url_create': f'{model}_create',
        'url_update': f'{model}_update',
        'url_delete': f'{model}_delete',
        'url_create_full': reverse( f'{model}_create'),

        'path_script': 'custom/js/entity.js',
        'path_table_body_fragment':  f'pages/parametrage/table_body_fragment/{model}.html',
        'path_table_body':  'partials/table_body/entity.html',
        'path_form_update': 'partials/entity_form/common/form_update.html',
        'path_form_create': 'partials/entity_form/common/form_create.html',
        'path_form_delete': 'partials/entity_form/common/form_delete.html',

        'table_header': (
            f"<tr>"
                "<th>#ID</th>"
                "<th>Type Apprentissage</th>"
                "<th>Libelle</th>"
                "<th>Description</th>"
                "<th>Action</th>"
              "</tr>"
        ),
    }
    print(genre)

    if key is None:
        return data
    return data.get(key, None)

def tache(request):
    
    items = Tache.objects.all()
    
    context = get_metadata()
    context['data'] = items
    
    return render(request, 'pages/parametrage/entity.html', context)


def save_entity_form(request, form, template_name):
    data = dict()
    context = get_metadata()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            items = Tache.objects.all()
            print(items)
            context['data'] = items
            data['html_entity_list'] = render_to_string(get_metadata('path_table_body'), context)
        else:
            data['form_is_valid'] = False
    
    context['form'] = form
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def tache_create(request):
    if request.method == 'POST':
        form = TacheForm(request.POST)
    else:
        form = TacheForm()
    
    return save_entity_form(request, form, get_metadata('path_form_create'))

def tache_update(request, pk):
    entity = get_object_or_404(Tache, pk=pk)
    if request.method == 'POST':
        form = TacheForm(request.POST, instance=entity)
    else:
        form = TacheForm(instance=entity)
    return save_entity_form(request, form, get_metadata('path_form_update'))

def tache_delete(request, pk):
    entity = get_object_or_404(Tache, pk=pk)
    data = dict()
    context = get_metadata()

    if request.method == 'POST':
        entity.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        items = Tache.objects.all()
        context['data'] = items
        data['html_entity_list'] = render_to_string(get_metadata('path_table_body'), context)
    else:
        context['entity'] = entity
        context['entity_name'] = str(entity)
        data['html_form'] = render_to_string(get_metadata('path_form_delete'), context, request=request, )
    print(str(entity))
    return JsonResponse(data)
