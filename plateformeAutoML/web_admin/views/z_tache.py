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
    data = {
        'model': model,
        'genre': 'F',
        'url_create': model + '_create',
        'url_update': model + '_update',
        'url_delete': model + '_delete',
        'path_script': 'custom/js/entity.js',
        'path_table_body':  'partials/table_body/tache.html',
        'path_form_update': 'partials/entity_form/common/form_update.html',
        'path_form_create': 'partials/entity_form/common/form_create.html',
        'path_form_delete': 'partials/entity_form/common/form_delete.html',
    }
    genre = 'F'
    print(genre)
    data['title_modal_create'] = 'Creer ' +  ('une nouvelle', 'un nouveau')[ genre == 'F']  + f' {model}'

    if key is None:
        return data
    return data.get(key, 'ok')

def tache(request):
    
    items = Tache.objects.all()
    
    context = get_metadata()
    context['data'] = items
    context['section_title'] = 'Parametrage'
    context['section_item_title'] = 'Taches de Machine Learning'
    context['url_create_full'] = reverse(context['url_create'])
    
    return render(request, 'pages/parametrage/tache.html', context)


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
    tache = get_object_or_404(Tache, pk=pk)
    if request.method == 'POST':
        form = TacheForm(request.POST, instance=tache)
    else:
        form = TacheForm(instance=tache)
    return save_entity_form(request, form, get_metadata('path_form_update'))

def tache_delete(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    data = dict()
    context = get_metadata()

    if request.method == 'POST':
        tache.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        items = Tache.objects.all()
        context['data'] = items
        data['html_entity_list'] = render_to_string(get_metadata('path_table_body'), context)
    else:
        context['entity'] = tache
        context['entity_name'] = str(tache)
        data['html_form'] = render_to_string(get_metadata('path_form_delete'), context, request=request, )
    print(str(tache))
    return JsonResponse(data)
