from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from web_admin.models import Metrique
from web_admin.forms import MetriqueForm
from web_admin.services import init_config as init

# Create your views here.

def get_metadata(key = None):

    model = 'metrique'
    genre = 'F'

    data = {
        'can_init': True,
        'can_add': False,
        'can_edit': True,
        'can_delete': False,

        'page_title': 'AutoML - Plateforme de Machine Learning Automaisé',
        'table_title': 'Liste des metriques',
        'section_title': 'Parametrage',
        'section_item_title': 'Imputatation',
     
        'title_modal_create': f'Creer {("une nouvelle", "un nouveau")[ genre == "F"]} {model}',
     
        'model': model,
        'genre': 'M',

        'url_create': f'{model}_update',
        'url_update': f'{model}_update',
        'url_delete': f'{model}_delete',
        # 'url_create_full': reverse( f'{model}_create'),

        'path_script': 'custom/js/entity.js',
        'path_table_body_fragment':  f'pages/parametrage/table_body_fragment/{model}.html',
        'path_table_body':  'partials/table_body/entity.html',
        'path_form_update': 'partials/entity_form/common/form_update.html',
        'path_form_create': 'partials/entity_form/common/form_create.html',
        'path_form_delete': 'partials/entity_form/common/form_delete.html',

        'table_header': (
            f"<tr>"
                "<th>#ID</th>"
                "<th>Tache</th>"
                "<th>Libelle</th>"
                "<th>Description</th>"
                "<th>Action</th>"
              "</tr>"
        ),
    }
    data['url_create'] = data['url_update']
    data['url_delete'] = data['url_update']
    data['url_create_full'] = data['url_update']
    print(genre)

    if key is None:
        return data
    return data.get(key, None)

def metrique(request):
    init.metrique()
    items = Metrique.objects.all()
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
            items = Metrique.objects.all()
            print(items)
            context['data'] = items
            data['html_entity_list'] = render_to_string(get_metadata('path_table_body'), context)
        else:
            data['form_is_valid'] = False
    
    context['form'] = form
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def metrique_update(request, pk):
    entity = get_object_or_404(Metrique, pk=pk)
    if request.method == 'POST':
        form = MetriqueForm(request.POST, instance=entity)
    else:
        form = MetriqueForm(instance=entity)
    return save_entity_form(request, form, get_metadata('path_form_update'))