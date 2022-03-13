from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from web_admin.models import Tache
# Create your views here.

def tache_metadata(key = None):

    model = 'tache'
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
    genre = 'F'
    print(genre)
    data['title_modal_create'] = 'Creer ' +  ('une nouvelle', 'un nouveau')[ genre == 'F']  + f' {model}'

    if key is None:
        return data
    return data.get(key, '')

def tache(request):
    
    items = Tache.objects.all()
    
    html_data = tache_metadata()
    html_data['data'] = items
    html_data['url_create_full'] = reverse(html_data['url_create'])
    
    return render(request, 'tache.html', html_data)


def save_tache_form(request, form, template_name, template_data=None):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            items = Tache.objects.all()
            data['html_tache_list'] = render_to_string(tache_metadata('path_table_body'), { 'data': items })
        else:
            data['form_is_valid'] = False
    template_data['form'] = form
    data['html_form'] = render_to_string(template_name, template_data, request=request)
    return JsonResponse(data)

def tache_create(request):
    data = tache_metadata()
    
    print(data['title_modal_create'])
    if request.method == 'POST':
        form = TacheForm(request.POST)
    else:
        form = TacheForm()
    
    return save_tache_form(request, form, tache_metadata('path_form_create'), data)

def tache_update(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    if request.method == 'POST':
        form = TacheForm(request.POST, instance=tache)
    else:
        form = TacheForm(instance=tache)
    return save_tache_form(request, form, tache_metadata('path_form_update'))

def tache_delete(request, pk):
    tache = get_object_or_404(Tache, pk=pk)
    data = dict()
    if request.method == 'POST':
        tache.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        items = Tache.objects.all()
        data['html_tache_list'] = render_to_string(tache_metadata('path_table_body'), { 'data': items })
    else:
        context = {'tache': tache}
        data['html_form'] = render_to_string(tache_metadata('path_form_delete'), context, request=request, )
    return JsonResponse(data)
