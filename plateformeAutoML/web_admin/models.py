from django.db import models
from .enum import ETypeDonnee, EEtatPublication, ETypeValeur
from django.urls import reverse

#todo
#TextFild Limitation

class Compte(models.Model):
    login = models.CharField(max_length=254, blank=True,null=True)
    prenom = models.CharField(max_length=254, blank=True,null=True)
    password = models.CharField(max_length=254, blank=True,null=True)
    est_active = models.BooleanField()
    etat = models.IntegerField(default=0, blank=True,null=True)


class Utilisateur(models.Model):
    nom = models.CharField(max_length=254, blank=True,null=True)
    prenom = models.CharField(max_length=254, blank=True,null=True)
    telephone = models.CharField(max_length=254, blank=True,null=True)
    email = models.EmailField(max_length=254, blank=True,null=True)
    pays = models.CharField(max_length=254, blank=True,null=True)

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


class SymboleValeurManquante(models.Model):
    symbole =  models.CharField(max_length=254, blank=True,null=True)


class CritereComparaison(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)


class Package(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)

class Famille(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)

class TypeApprentissage(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)

class Tache(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    type_apprentissage = models.ForeignKey(TypeApprentissage, on_delete=models.CASCADE)


class Algorithme(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE)
    famille = models.ForeignKey(Famille, on_delete=models.CASCADE)
    projet = models.ManyToManyField(Projet,through='AlgorithmeProjet')


class Metrique(models.Model):
    libele =  models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254,blank=True,null=True)
    algorithmes = models.ManyToManyField(Algorithme,through='MetriqueAlgorithme')


class AlgorithmeProjet(models.Model):
    libele =  models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    nombre_modele = models.IntegerField(default=0, blank=True,null=True)
    algorthme = models.ForeignKey(Algorithme, on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    metriques = models.ManyToManyField(Metrique,through='MetriqueAlgorithmeProjet')

class Modele(models.Model):
    chemin =  models.CharField(max_length=254, blank=True,null=True)
    precision =  models.CharField(max_length=254, blank=True,null=True)
    rapport = models.TextField(max_length=254, blank=True,null=True)
    resume = models.TextField(max_length=254, blank=True,null=True)
    algorithme_projet = models.ForeignKey(AlgorithmeProjet, on_delete=models.CASCADE)


class Parametre(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    type = models.CharField(max_length=50, choices=ETypeDonnee.choices(), default=ETypeDonnee.DECIMAL)
    modele = models.ForeignKey(Modele, on_delete=models.CASCADE)

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

# à revoir 


class TaxionomieTypeDonne(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)


class Encodage(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    strategie_encodages = models.ManyToManyField(TaxionomieTypeDonne, through='StrategieEncodage')


class StrategieEncodage(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    encodage = models.ForeignKey(Encodage, on_delete=models.CASCADE)
    taxionomie_type_donne = models.ForeignKey(TaxionomieTypeDonne, on_delete=models.CASCADE)

class Imputation(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    taxionomie_type_donnes = models.ManyToManyField(TaxionomieTypeDonne, through='StrategieImputation')

class StrategieImputation(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    imputation = models.ForeignKey(Imputation, on_delete=models.CASCADE)
    taxionomie_type_donnee = models.ForeignKey(TaxionomieTypeDonne, on_delete=models.CASCADE)

class MiseEchelle(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    taxionomie_type_donnes = models.ManyToManyField(TaxionomieTypeDonne, through='StrategieMiseEchelle')


class StrategieMiseEchelle(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.TextField(max_length=254, blank=True,null=True)
    taxionomie_type_donnee = models.ForeignKey(TaxionomieTypeDonne, on_delete=models.CASCADE)
    mise_echelle = models.ForeignKey(MiseEchelle, on_delete=models.CASCADE)
    

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

# Create your models here.
