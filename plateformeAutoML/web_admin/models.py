from django.db import models
from .enum import ETypeDonnee, EEtatPublication, ENatureValeur, EEtatCompte
from django.urls import reverse
from web_admin.managers import CompteManager, ModelManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from django.utils.text import slugify

#from django.contrib.postgres.fields import ArrayField


class Compte(AbstractBaseUser, PermissionsMixin):
    code =  models.CharField(max_length=254, blank=True,null=True)
    login = models.CharField(max_length=70, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=250)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_adhesion = models.DateTimeField(default=now)
    etat = models.CharField(max_length=50, choices=EEtatCompte.choices(), default=EEtatCompte.ACTIF)

    USERNAME_FIELD = 'login'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email','telephone']

    objects = CompteManager()

    # def __str__(self):
    #     return self.login

class Utilisateur(models.Model):
    code =  models.CharField(max_length=254, blank=True,null=True)
    nom = models.CharField(max_length=70, blank=True,null=True)
    prenom = models.CharField(max_length=70, blank=True,null=True)
    telephone = models.CharField(max_length=254, blank=True,null=True)
    pays = models.CharField(max_length=254, blank=True,null=True)
    ville = models.CharField(max_length=254, blank=True,null=True)
    compte = models.OneToOneField( Compte, on_delete=models.CASCADE, primary_key=True,)
    description  =  models.TextField(max_length=254, blank=True, default='')
    
    def __str__(self):
        return "%s  %s" % (self.prenom, self.nom)

class Projet(models.Model):
    code =  models.CharField(max_length=254, blank=True,null=True)
    titre =  models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')
    mots_cles  =  models.TextField(max_length=254, blank=True, default='')
    metrique =  models.CharField(max_length=254, blank=True,null=True) #to del
    image = models.ImageField(upload_to="projet/image/%Y/%m/%d")
    # type = models.CharField(max_length=50, choices=ETypeDonnee.choices(), default=ETypeDonnee.DECIMAL)
    statut = models.CharField(max_length=50, choices=EEtatPublication.choices(), default=EEtatPublication.PRIVE)
    nombre_modele = models.IntegerField(default=0, blank=True,null=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    
    slug = models.SlugField(null=True, unique=True) #slud automatic

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('projet_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.titre)
        return super().save(*args, **kwargs)

class JeuDonnees(models.Model):
    code =  models.CharField(max_length=254, blank=True,null=True)
    fichier =  models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='', null=True)
    source =  models.CharField(max_length=254, blank=True,null=True)
    pourcentage_validation = models.DecimalField(default=0,  max_digits=3, decimal_places=2, blank=True,null=True)
    pourcentage_entrainement = models.DecimalField(default=0,  max_digits=3, decimal_places=2, blank=True,null=True)
    pourcentage_test = models.DecimalField(default=0.3,  max_digits=3, decimal_places=2, blank=True,null=True)
    taille = models.IntegerField(default=0, blank=True,null=True)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    # compte = models.OneToOneField( Compte, on_delete=models.CASCADE, primary_key=True,)


    def __str__(self):
        return self.fichier


class SymboleValeurManquante(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    symbole =  models.CharField(max_length=254, blank=True,null=True)

    def __str__(self):
        return self.symbole


class CritereComparaison(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')

    def __str__(self):
        return self.libelle


class Package(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')

    def __str__(self):
        return self.libelle

class Famille(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')

    def __str__(self):
        return self.libelle

class TypeApprentissage(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')

    def __str__(self):
        return self.libelle

class Tache(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')
    type_apprentissage = models.ForeignKey(TypeApprentissage, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Tache._meta.fields]


class Algorithme(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE, null=True)
    famille = models.ForeignKey(Famille, on_delete=models.CASCADE, null=True)   
    projet = models.ManyToManyField(Projet,through='AlgorithmeProjet') # (fields.W340) null has no effect on ManyToManyField.

    def __str__(self):
        return self.libelle

class Metrique(models.Model):
    code =  models.CharField(max_length=254, blank=True,null=True)
    libelle =  models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')
    # algorithmes = models.ManyToManyField(Algorithme,through='MetriqueAlgorithme')
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle

class AlgorithmeProjet(models.Model):
    code =  models.CharField(max_length=254, blank=True,null=True)
    algorithme = models.ForeignKey(Algorithme, on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    metrique = models.ForeignKey(Metrique, on_delete=models.CASCADE, null=True)   
    # metriques = models.ManyToManyField(Metrique,through='MetriqueAlgorithmeProjet')

    """def __str__(self):
        return self.alg"""

class Modele(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    chemin =  models.CharField(max_length=254, blank=True,null=True)
    precision =  models.CharField(max_length=254, blank=True,null=True)
    rapport = models.TextField(max_length=254, blank=True,null=True)
    resume = models.TextField(max_length=254, blank=True,null=True)
    algorithme_projet = models.ForeignKey(AlgorithmeProjet, on_delete=models.CASCADE)
    jeu_donnees = models.ForeignKey(JeuDonnees, on_delete=models.CASCADE)

    def __str__(self):
        return self.resume

class Parametre(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')
    type = models.CharField(max_length=50, choices=ETypeDonnee.choices(), default=ETypeDonnee.DECIMAL)
    modele = models.ForeignKey(Modele, on_delete=models.CASCADE)

    def __str__(self):
        return self.libelle

# class MetriqueAlgorithme(models.Model):
#     code = models.CharField(max_length=254, blank=True,null=True)
#     metrique = models.ForeignKey(Metrique, on_delete=models.CASCADE)
#     algorithme = models.ForeignKey(Algorithme, on_delete=models.CASCADE)


# class MetriqueAlgorithmeProjet(models.Model):
#     code = models.CharField(max_length=254, blank=True,null=True)
#     metrique = models.ForeignKey(Metrique, on_delete=models.CASCADE)
#     algorithme_projet = models.ForeignKey(AlgorithmeProjet, on_delete=models.CASCADE)


class CritereComparaisonAlgorithme(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    valeur = models.IntegerField(default=0, blank=True,null=True)
    min = models.IntegerField(default=0, blank=True,null=True)
    max = models.IntegerField(default=0, blank=True,null=True)
    critere_comparaison = models.ForeignKey(CritereComparaison, on_delete=models.CASCADE)
    algorithme = models.ForeignKey(Algorithme, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.libelle} : [{self.min}, {self.max}]'

#à revoir 


class TaxonomieTypeDonnee(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')

    def __str__(self):
        return self.libelle

class Encodage(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')
    strategie_encodages = models.ManyToManyField(TaxonomieTypeDonnee, through='StrategieEncodage')

    objects = ModelManager()


    def __str__(self):
        return self.libelle

class StrategieEncodage(models.Model):
    # code = models.CharField(max_length=254, blank=True,null=True)
    # libelle = models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')
    encodage = models.ForeignKey(Encodage, on_delete=models.CASCADE, null=True)
    taxonomie_type_donnee = models.ForeignKey(TaxonomieTypeDonnee, on_delete=models.CASCADE)
    # is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.libelle

class Imputation(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')
    taxionomie_type_donnes = models.ManyToManyField(TaxonomieTypeDonnee, through='StrategieImputation')

    objects = ModelManager()

    def __str__(self):
        return self.libelle

class StrategieImputation(models.Model):
    # code = models.CharField(max_length=254, blank=True,null=True)
    # libelle = models.CharField(max_length=254, blank=True,null=True)
    taxonomie_type_donnee = models.ForeignKey(TaxonomieTypeDonnee, on_delete=models.CASCADE)
    imputation = models.ForeignKey(Imputation, on_delete=models.CASCADE, null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')
    # is_default = models.BooleanField(default=False)


    def __str__(self):
        return str(self.taxonomie_type_donnee)

class MiseEchelle(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')
    taxionomie_type_donnes = models.ManyToManyField(TaxonomieTypeDonnee, through='StrategieMiseEchelle')

    objects = ModelManager()

    def __str__(self):
        return self.libelle

class StrategieMiseEchelle(models.Model):
    # code = models.CharField(max_length=254, blank=True,null=True)
    # libelle = models.CharField(max_length=254, blank=True,null=True)
    description  =  models.TextField(max_length=254, blank=True, default='')
    taxonomie_type_donnee = models.ForeignKey(TaxonomieTypeDonnee, on_delete=models.CASCADE)
    mise_echelle = models.ForeignKey(MiseEchelle, on_delete=models.CASCADE, null=True)
    # is_default = models.BooleanField(default=False)
    
    def __str__(self):
        return self.libelle

class Colonne(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    libelle = models.CharField(max_length=254, blank=True)
    type_donnees = models.CharField(max_length=50, choices=ETypeDonnee.choices(), default=ETypeDonnee.DECIMAL.value)
    est_categoriel = models.BooleanField(default=False)
    est_target  = models.BooleanField(default=False)
    est_selectionnee = models.BooleanField(default=True)
    pattern = models.CharField(max_length=254, blank=True,null=True)
    # valeurs = ArrayField(models.CharField(max_length=100), null=True)
    array_valeurs = list()
    valeurs = models.CharField(max_length=10000, blank=True,null=True)
    jeu_donnees = models.ForeignKey(JeuDonnees, on_delete=models.CASCADE, null=False, blank=False)

    encodage = models.ForeignKey(Encodage, on_delete=models.CASCADE, null=True)
    imputation = models.ForeignKey(Imputation, on_delete=models.CASCADE, null=True)
    normalisation = models.ForeignKey(MiseEchelle, on_delete=models.CASCADE, null=True)

    objects = ModelManager()

    def __str__(self):
        return self.libelle

class HyperParametre(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    valeur_defaut = models.CharField(max_length=254, blank=True,null=True)
    cle =  models.CharField(max_length=254, blank=True,null=True)
    type_donnees = models.CharField(max_length=50, choices=ETypeDonnee.choices(), default=ETypeDonnee.DECIMAL)
    valeurs = models.ManyToManyField(AlgorithmeProjet, through='Valeur')

    def __str__(self):
        return "{0} : {1}".format(self.cle, self.valeur) 
        
class Valeur(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    algorithme_projet = models.ForeignKey(AlgorithmeProjet, on_delete=models.CASCADE)
    hyper_parametre = models.ForeignKey(HyperParametre, on_delete=models.CASCADE)
    contenu = models.TextField(max_length=254, blank=True,null=True)

    def __str__(self):
        return self.contenu



class Fichier(models.Model):
    code = models.CharField(max_length=254, blank=True,null=True)
    chemin = models.CharField(max_length=100)
    nom = models.CharField(max_length=50)
    eof = models.BooleanField()

class Configuration():
    has_init = models.BooleanField(default=False)
    description =  models.CharField(max_length=254, blank=True,null=True)
    has_update = models.BooleanField(default=False)
    last_update = models.DateTimeField(default=now)

    # def __str__(self):
    #     return self.description

class TableModel:
    class Meta:
       managed = False
       
    def __init__(self,id,algo,code,precision,famille):
        self.id = id
        self.algo = algo
        self.code = code
        self.precision = precision
        self.famille = famille
# Create your models here.
