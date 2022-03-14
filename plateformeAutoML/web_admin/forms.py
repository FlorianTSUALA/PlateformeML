from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
import datetime
from django.contrib.admin import widgets
from django.forms.widgets import NumberInput
from web_admin.models import  TypeApprentissage, Tache #,Compte, Profile

# class CompteCreationForm(UserCreationForm):
    
#     class Meta:
#         model = Compte
#         fields = ['username', 'telephone', 'email', 'name', 'password1', 'password2']

#     def __init__(self, *args, **kwargs):
#         super(CompteCreationForm, self).__init__(*args, **kwargs)
        
#         self.fields['username'].widget.attrs['placeholder'] = 'Login'

# class CompteChangeForm(UserChangeForm):

#     class Meta:
#         model = Compte
#         fields = ('username', 'telephone', 'email', 'name')

class TacheForm(forms.ModelForm):

    class Meta:
        model = Tache
        fields = (
            'type_apprentissage',
            'libelle',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(TacheForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            
            new_data = {
                "class": 'form-control',
            }

            self.fields[str(field)].widget.attrs.update(
                new_data
            )

            if field == 'type_apprentissage':
                pass

        # self.fields['date_naissance'].widget.input_type = 'date'

        self.fields['type_apprentissage'].widget.attrs['class'] = 'form-control select2'
        self.fields['type_apprentissage'].widget.attrs['style'] = 'width: 100%;'
        self.fields['type_apprentissage'].initial = 'choisir une valeur'

        self.fields['description'].widget.attrs.update({'rows': '2'})

class TypeApprentissageForm(forms.ModelForm):

    class Meta:
        model = TypeApprentissage
        fields = (
            'libelle',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(TypeApprentissageForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            
            new_data = {
                "class": 'form-control',
            }

            self.fields[str(field)].widget.attrs.update(
                new_data
            )
        self.fields['description'].widget.attrs.update({'rows': '2'})
