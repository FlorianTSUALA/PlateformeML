from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from access_control.models import Gestionnaire, Compte
from access_control.forms import GestionnaireForm, CompteCreationForm
import hashlib, binascii
from django.contrib.auth import (authenticate, login, logout, get_user_model, REDIRECT_FIELD_NAME)
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, Permission
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.conf import settings

# # Create your views here.
# class IndexView(TemplateView):
#     template_name = 'index.html'
    
# class Login(LoginView):
#     template_name = 'registration/login.html'

class RegisterView(FormView):
    form_class = CompteCreationForm
    template_name = 'auth/auth_register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)

def register(request):
    print('registration')
    if request.method == "POST":
        username = request.POST.get('username')
        nom = request.POST.get('nom')
        telephone = request.POST.get('telephone')
        email = request.POST.get('email')
        pwd1 = request.POST.get('passw1')
        pwd2 = request.POST.get('passw2')
        if pwd1 !=pwd2:
            message = 'Les mots de passes ne sont pas identique'
            return render(request,'auth/auth_register.html',{'message':message})
        else:
           dk = hashlib.pbkdf2_hmac('sha256', str.encode(pwd1), b'salt', 10000)
           password = binascii.hexlify(dk)
           compte = Compte(
                            email = email,
                            name = nom,
                            username = username,
                            telephone = telephone,
                            password = password
                        )
           compte.save()
           return redirect(settings.LOGIN_URL)

            # messages.error(request, 'creation de compte échouée')
            # render(request,'users/register.html',{'form':form})
    else:
        return render(request, 'auth/auth_register.html')
        
    return render(request,'auth/auth_register.html')


def user_login(request):
    redirect_to = request.POST.get(REDIRECT_FIELD_NAME, request.GET.get(REDIRECT_FIELD_NAME, reverse('gestionnaire')))

    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to)

    if request.method == "POST":
        
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        remember_me = request.POST.get('remember_me')

        try:
            utilisateur = Compte.objects.get(username=username)
        except ObjectDoesNotExist:
            message = 'Votre identifiant ou votre mot de passe est incorrect'
            return render(request,'auth/auth_login.html',{'message':message})
        
        dk = hashlib.pbkdf2_hmac('sha256', str.encode(pwd), b'salt', 10000)
        password = binascii.hexlify(dk)

        print("User Active State : ", utilisateur.is_active)

        if str(password) == str(utilisateur.password):
            if  utilisateur.is_active:
                # The default Django's "remember me" lifetime is 2 weeks and can be changed by modifying
                # the SESSION_COOKIE_AGE settings' option.
                if settings.USE_REMEMBER_ME:
                    if not remember_me:
                        request.session.set_expiry(0)
                login(request, utilisateur)
                return redirect(redirect_to)
            else:
                pass
        else:
            message = 'Votre identifiant ou votre mot de passe est incorrect'
            return render(request,'auth/auth_login.html',{'message':message})
    else:
        return render(request, 'auth/auth_login.html')

def user_logout(request):
    if not request.user.is_authenticated:
        logout(request)
    return redirect(settings.LOGIN_URL)



def check_username(request):
    print('Request check')
    username = request.POST.get('username', None)
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("<span id='username-error' class='help-block text-warning'>This username already exists</span>")
    else:
        return HttpResponse("<span id='username-error' class='help-block text-success'>This username is available</span>")
