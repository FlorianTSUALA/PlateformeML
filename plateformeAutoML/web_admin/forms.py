from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
import datetime
from django.contrib.admin import widgets
from django.forms.widgets import NumberInput
from web_admin.models import  TypeApprentissage, Tache, CritereComparaison, Package, Famille, Algorithme,TaxonomieTypeDonnee #,Compte, Profile

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

class CritereComparaisonForm(forms.ModelForm):

    class Meta:
        model = CritereComparaison
        fields = (
            'libelle',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(CritereComparaisonForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            
            new_data = {
                "class": 'form-control',
            }

            self.fields[str(field)].widget.attrs.update(
                new_data
            )
        self.fields['description'].widget.attrs.update({'rows': '2'})

class AlgorithmeForm(forms.ModelForm):

    class Meta:
        model = Algorithme
        fields = (
            'libelle',
            'package',
            'tache',
            'famille',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(AlgorithmeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            
            new_data = {
                "class": 'form-control',
            }

            self.fields[str(field)].widget.attrs.update(
                new_data
            )
        
        self.fields['tache'].widget.attrs['class'] = 'form-control select2'
        self.fields['tache'].widget.attrs['style'] = 'width: 100%;'
        self.fields['tache'].initial = 'choisir une valeur'

        
        self.fields['famille'].widget.attrs['class'] = 'form-control select2'
        self.fields['famille'].widget.attrs['style'] = 'width: 100%;'
        self.fields['famille'].initial = 'choisir une valeur'

        
        self.fields['package'].widget.attrs['class'] = 'form-control select2'
        self.fields['package'].widget.attrs['style'] = 'width: 100%;'
        self.fields['package'].initial = 'choisir une valeur'

        self.fields['description'].widget.attrs.update({'rows': '2'})

class FamilleForm(forms.ModelForm):

    class Meta:
        model = Famille
        fields = (
            'libelle',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(FamilleForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            
            new_data = {
                "class": 'form-control',
            }

            self.fields[str(field)].widget.attrs.update(
                new_data
            )
        self.fields['description'].widget.attrs.update({'rows': '2'})

class PackageForm(forms.ModelForm):

    class Meta:
        model = Package
        fields = (
            'libelle',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(PackageForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            
            new_data = {
                "class": 'form-control',
            }

            self.fields[str(field)].widget.attrs.update(
                new_data
            )
        self.fields['description'].widget.attrs.update({'rows': '2'})


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

class TaxonomieTypeDonneeForm(forms.ModelForm):

    class Meta:
        model = TaxonomieTypeDonnee
        fields = (
            'libelle',
            'description',
        )

    def __init__(self, *args, **kwargs):
        super(TaxonomieTypeDonneeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            
            new_data = {
                "class": 'form-control',
            }

            self.fields[str(field)].widget.attrs.update(
                new_data
            )
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
