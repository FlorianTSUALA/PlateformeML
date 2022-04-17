from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import TemplateView
from web_admin.models import Compte, Utilisateur
from django.contrib.auth.decorators import login_required


def profile(request):
    if request.user.is_authenticated:
        username = request.user.utilisateur.nom
        print('USERNAME : ', username)

    context = dict()
    context['has_white_text'] = True
    context['section_title'] = 'Profile Utilisateur'
    context['section_item_title'] = 'Mon Compte'
    context['utilisateur'] = request.user.utilisateur
    return render(request, 'pages/profile/profile.html', context)


def profile_list(request, filter):
    context = dict()
    context['has_white_text'] = True
    context['section_title'] = 'Profile Utilisateur'
    context['section_item_title'] = 'Liste'
    # context['profiles'] = Utilisateur.objects.all(compte.etat=filter)
    context['profiles'] = Utilisateur.objects.all()

    # if request.user.is_authenticated():
    #     username = request.user.username
    #     print('USERNAME : ', username)
    return render(request, 'pages/profile/profile_list.html', context)

def profile_create(request):
    context = {}
    context['has_white_text'] = True
    context['section_title'] = 'Utilisateur'
    context['section_item_title'] = 'Mon Compte'

    print('registration')
    if request.method == "POST":
        login = request.POST.get('login')
        email = request.POST.get('email')
        pwd1 = request.POST.get('pwd1')
        pwd2 = request.POST.get('pwd2')

        if pwd1 !=pwd2:
            message = 'Les mots de passes ne sont pas identiques'
            return render(request, 'pages/profile/profile_create.html')
        else:
           dk = hashlib.pbkdf2_hmac('sha256', str.encode(pwd1), b'salt', 10000)
           password = binascii.hexlify(dk)
           compte = Compte(
                            login = login,
                            email = email,
                            password = password
                        )
           compte.save()
           utilisateur = Utilisateur(
                            compte = compte,
                            nom = request.POST.get('nom'),
                            prenom = request.POST.get('prenom'),
                            telephone = request.POST.get('telephone'),
                            pays = request.POST.get('pays'),
                            ville = request.POST.get('ville'),
                            description = request.POST.get('description'),
            )
           utilisateur.save()
           return redirect(liste)
    else:
        return render(request, 'pages/profile/profile_create.html', context)
        
    return render(request,'pages/profile/profile_create.html', context)

def profile_update(request):
    if request.method == "POST":
        id_compte = request.POST.get('id_compte')

        compte = Compte.objects.get(id = id_compte)
        utilisateur = Utilisateur.objects.get(compte_id = id_compte)
        compte.login = request.POST.get('login')
        compte.email = request.POST.get('email')
        utilisateur.nom = request.POST.get('nom')
        utilisateur.prenom = request.POST.get('prenom')
        utilisateur.telephone = request.POST.get('telephone')
        utilisateur.pays = request.POST.get('pays')
        utilisateur.ville = request.POST.get('ville')
        utilisateur.description = request.POST.get('description')

        compte.save(update_fields=['login','email'])
        utilisateur.save(update_fields=['nom','prenom','telephone','pays','ville', 'description'])

    return redirect(profile)

def profile_delete(request, pk):
    entity = get_object_or_404(Utilisateur, compte_id=pk)
    entity.delete()
    return redirect(profile_list)