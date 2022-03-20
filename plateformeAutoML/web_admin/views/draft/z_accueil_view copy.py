from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from web_admin.models import Permission
from web_admin.forms import ProfileForm

def profile_metadata(key = None):

    model = 'profile'
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


def add_profile(request):
    name = request.GET.get('name')
    profile = Profile.objects.create(name=name)

    # request.user.profile.add(profile)
    profiles = Profile.objects.all()
    return render(request, 'includes/profile-list.html',{profiles: profiles})



def profile(request):
    items = Permission.objects.all()
    
    html_data = profile_metadata()
    html_data['data'] = items
    html_data['url_create_full'] = reverse(html_data['url_create'])
    
    return render(request, 'profile.html', html_data)



def save_profile_form(request, form, template_name, template_data={}):
    data = profile_metadata()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            items = Profile.objects.all()
            data['html_profile_list'] = render_to_string(profile_metadata('path_table_body'), { 'data': items })
        else:
            data['form_is_valid'] = False
    template_data['form'] = form
    # html_data = profile_metadata()
    data['html_form'] = render_to_string(template_name, template_data, request=request)
    return JsonResponse(data)

def profile_create(request):
    data = profile_metadata()
    
    if request.method == 'POST':
        form = ProfileForm(request.POST)
    else:
        form = ProfileForm()
    
    return save_profile_form(request, form, profile_metadata('path_form_create'), data)

def profile_update(request, pk):
    profile = get_object_or_404(profile, pk=pk)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
    else:
        form = ProfileForm(instance=profile)
    return save_profile_form(request, form, profile_metadata('path_form_update'))

def profile_delete(request, pk):
    profile = get_object_or_404(profile, pk=pk)
    data = profile_metadata()
    if request.method == 'POST':
        profile.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        items = Profile.objects.all()
        data['html_profile_list'] = render_to_string(profile_metadata('path_table_body'), { 'data': items })
    else:
        context = {'profile': profile}
        data['html_form'] = render_to_string(profile_metadata('path_form_delete'), context, request=request, )
    return JsonResponse(data)
