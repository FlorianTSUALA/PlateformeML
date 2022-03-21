from django.db import models
from .enum import ETypeDonnee, EEtatPublication, ETypeValeur
from django.urls import reverse
from web_admin.managers import CompteManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

class Compte(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(max_length=70, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=250)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_adhesion = models.DateTimeField(default=now)
    etat = models.IntegerField(default=0, blank=True,null=True) #Enumeration attente_validation,...

    USERNAME_FIELD = 'login'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email','telephone']

    objects = CompteManager()

    # def __str__(self):
    #     return self.login

class Utilisateur(models.Model):
    nom = models.CharField(max_length=70, blank=True,null=True)
    prenom = models.CharField(max_length=70, blank=True,null=True)
    telephone = models.CharField(max_length=254, blank=True,null=True)
    pays = models.CharField(max_length=254, blank=True,null=True)
    ville = models.CharField(max_length=254, blank=True,null=True)
    compte = models.OneToOneField( Compte, on_delete=models.CASCADE, primary_key=True,)
    decription = models.TextField(blank=True,null=True)

    def __str__(self):
        return "%s  %s" % (self.prenom, self.nom)

class Projet(models.Model):
    title =  models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    metrique =  models.CharField(max_length=254, blank=True,null=True) #to del
    type = models.CharField(max_length=50, choices=ETypeDonnee.choices(), default=ETypeDonnee.DECIMAL)
    est_publique = models.CharField(max_length=50, choices=EEtatPublication.choices(), default=EEtatPublication.PRIVE)
    nombre_modele = models.IntegerField(default=0, blank=True,null=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('projet_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class JeuDonnees(models.Model):
    fichier =  models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    source =  models.CharField(max_length=254, blank=True,null=True)
    pourcentage_validation = models.DecimalField(default=0,  max_digits=3, decimal_places=2, blank=True,null=True)
    pourcentage_test = models.DecimalField(default=0.3,  max_digits=3, decimal_places=2, blank=True,null=True)
    taille = models.IntegerField(default=0, blank=True,null=True)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)

    def __str__(self):
        return self.fichier


class SymboleValeurManquante(models.Model):
    symbole =  models.CharField(max_length=254, blank=True,null=True)

    def __str__(self):
        return self.symbole


class CritereComparaison(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)

    def __str__(self):
        return self.libelle


class Package(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)

    def __str__(self):
        return self.libelle

class Famille(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)

    def __str__(self):
        return self.libelle

class TypeApprentissage(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)

    def __str__(self):
        return self.libelle

class Tache(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    type_apprentissage = models.ForeignKey(TypeApprentissage, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Tache._meta.fields]


class Algorithme(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE)
    famille = models.ForeignKey(Famille, on_delete=models.CASCADE)
    projet = models.ManyToManyField(Projet,through='AlgorithmeProjet')

    def __str__(self):
        return self.libelle

class Metrique(models.Model):
    libele =  models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254,blank=True,null=True)
    algorithmes = models.ManyToManyField(Algorithme,through='MetriqueAlgorithme')

    def __str__(self):
        return self.libelle

class AlgorithmeProjet(models.Model):
    libele =  models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    nombre_modele = models.IntegerField(default=0, blank=True,null=True)
    algorthme = models.ForeignKey(Algorithme, on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    metriques = models.ManyToManyField(Metrique,through='MetriqueAlgorithmeProjet')

    def __str__(self):
        return self.libelle

class Modele(models.Model):
    chemin =  models.CharField(max_length=254, blank=True,null=True)
    precision =  models.CharField(max_length=254, blank=True,null=True)
    rapport = models.TextField(max_length=254, blank=True,null=True)
    resume = models.TextField(max_length=254, blank=True,null=True)
    algorithme_projet = models.ForeignKey(AlgorithmeProjet, on_delete=models.CASCADE)

    def __str__(self):
        return self.resume

class Parametre(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    type = models.CharField(max_length=50, choices=ETypeDonnee.choices(), default=ETypeDonnee.DECIMAL)
    modele = models.ForeignKey(Modele, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle

class MetriqueAlgorithme(models.Model):
    metrique = models.ForeignKey(Metrique, on_delete=models.CASCADE)
    algorithme = models.ForeignKey(Algorithme, on_delete=models.CASCADE)


class MetriqueAlgorithmeProjet(models.Model):
    metrique = models.ForeignKey(Metrique, on_delete=models.CASCADE)
    algorithme_projet = models.ForeignKey(AlgorithmeProjet, on_delete=models.CASCADE)


class CritereComparaisonAlgorithme(models.Model):
    valeur = models.IntegerField(default=0, blank=True,null=True)
    min = models.IntegerField(default=0, blank=True,null=True)
    max = models.IntegerField(default=0, blank=True,null=True)
    critere_comparaison = models.ForeignKey(CritereComparaison, on_delete=models.CASCADE)
    algorithme = models.ForeignKey(Algorithme, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.libelle} : [{self.min}, {self.max}]'

# à revoir 


class TaxonomieTypeDonnee(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)

    def __str__(self):
        return self.libelle

class Encodage(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    strategie_encodages = models.ManyToManyField(TaxonomieTypeDonnee, through='StrategieEncodage')

    def __str__(self):
        return self.libelle

class StrategieEncodage(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    encodage = models.ForeignKey(Encodage, on_delete=models.CASCADE)
    taxionomie_type_donne = models.ForeignKey(TaxonomieTypeDonnee, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle

class Imputation(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    taxionomie_type_donnes = models.ManyToManyField(TaxonomieTypeDonnee, through='StrategieImputation')

    def __str__(self):
        return self.libelle

class StrategieImputation(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    imputation = models.ForeignKey(Imputation, on_delete=models.CASCADE)
    taxionomie_type_donnee = models.ForeignKey(TaxonomieTypeDonnee, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle

class MiseEchelle(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    taxionomie_type_donnes = models.ManyToManyField(TaxonomieTypeDonnee, through='StrategieMiseEchelle')

    def __str__(self):
        return self.libelle

class StrategieMiseEchelle(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    taxionomie_type_donnee = models.ForeignKey(TaxonomieTypeDonnee, on_delete=models.CASCADE)
    mise_echelle = models.ForeignKey(MiseEchelle, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.libelle

class Colonne(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    type_donnee = models.CharField(max_length=50, choices=ETypeDonnee.choices(), default=ETypeDonnee.DECIMAL)
    est_categoriel = models.BooleanField()
    est_target  = models.BooleanField()
    est_selectionnee = models.BooleanField()
    pattern = models.CharField(max_length=254, blank=True,null=True)
    jeu_donnees = models.ForeignKey(JeuDonnees, on_delete=models.CASCADE)
    strategie_encodage = models.ForeignKey(StrategieEncodage, on_delete=models.CASCADE)
    strategie_imputation = models.ForeignKey(StrategieImputation, on_delete=models.CASCADE)
    strategie_mise_echelle = models.ForeignKey(StrategieMiseEchelle, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle

class HyperParametre(models.Model):
    valeur_defaut = models.CharField(max_length=254, blank=True,null=True)
    cle =  models.CharField(max_length=254, blank=True,null=True)
    type_donnee = models.CharField(max_length=50, choices=ETypeDonnee.choices(), default=ETypeDonnee.DECIMAL)
    valeurs = models.ManyToManyField(AlgorithmeProjet, through='Valeur')

    def __str__(self):
        return "{0} : {1}".format(self.cle, self.valeur) 
        
class Valeur(models.Model):
    algorithme_projet = models.ForeignKey(AlgorithmeProjet, on_delete=models.CASCADE)
    hyper_parametre = models.ForeignKey(HyperParametre, on_delete=models.CASCADE)
    contenu = models.TextField(max_length=254, blank=True,null=True)

    def __str__(self):
        return self.contenu



class Fichier(models.Model):
    chemin = models.CharField(unique=True, max_length=100)
    nom = models.CharField(max_length=50)
    eof = models.BooleanField()

# Create your models here.
