from django.db import models
from django.db.models.enums import TextChoices


class Compte(models.Model):
    ligin = models.CharField(max_length=254, blank=True,null=True)
    prenom = models.CharField(max_length=254, blank=True,null=True)
    password = models.CharField(max_length=254, blank=True,null=True)
    estactive = models.IntegerField(max_length=254, blank=True,null=True)
    etat = models.IntegerField(max_length=254, blank=True,null=True)


class Utilisateur(models.Model):
    nom = models.CharField(max_length=254, blank=True,null=True)
    prenom = models.CharField(max_length=254, blank=True,null=True)
    telephone = models.CharField(max_length=254, blank=True,null=True)
    email = models.EmailField(max_length=254, blank=True,null=True)
    pays = models.CharField(max_length=254, blank=True,null=True)

class Projet(models.Model):
    nom =  models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)
    metrique =  models.CharField(max_length=254, blank=True,null=True)
    estPublic = models.CharField(max_length=254, blank=True,null=True)
    nbremodel = models.IntegerField(max_length=254, blank=True,null=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)



class JeuDonnees(models.Model):
    fichier =  models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)
    source =  models.CharField(max_length=254, blank=True,null=True)
    pourcentagevalidation = models.IntegerField(max_length=254, blank=True,null=True)
    pourcentagetest = models.IntegerField(max_length=254, blank=True,null=True)
    taille = models.IntegerField(max_length=254, blank=True,null=True)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)


class SymboleValeurManquant(models.Model):
    symbole =  models.CharField(max_length=254, blank=True,null=True)


class AlgorithmeProjet(models.Model):
    libele =  models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)
    nbremodele = models.IntegerField(max_length=254, blank=True,null=True)

class Metrique(models.Model):
    libele =  models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)
    algorithme_projet = models.ManyToManyField(AlgorithmeProjet)

class Modele(models.Model):
    chemin =  models.CharField(max_length=254, blank=True,null=True)
    precision =  models.CharField(max_length=254, blank=True,null=True)
    rapport = models.TextField(max_length=254, blank=True,null=True)
    resume = models.TextField(max_length=254, blank=True,null=True)
    algorithme_projet = models.ForeignKey(AlgorithmeProjet, on_delete=models.CASCADE)


class Parametre(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)
    type =  models.TextField(max_length=254, blank=True,null=True)
    modele = models.ForeignKey(Modele, on_delete=models.CASCADE)



class CritereComparaison(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)


class Package(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)

class Famille(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)

class TypeApprentissage(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)

class Tache(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)
    type_apprentissage = models.ForeignKey(TypeApprentissage, on_delete=models.CASCADE)


class Algorithme(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    tache = models.ForeignKey(Tache, on_delete=models.CASCADE)
    famille = models.ForeignKey(Famille, on_delete=models.CASCADE)

class CritereComparaisonAlgorithme(models.Model):
    valeur = models.IntegerField(max_length=254, blank=True,null=True)
    min = models.IntegerField(max_length=254, blank=True,null=True)
    max = models.IntegerField(max_length=254, blank=True,null=True)
    critere_comparaison = models.ForeignKey(CritereComparaison, on_delete=models.CASCADE)
    algorithme = models.ForeignKey(Algorithme, on_delete=models.CASCADE)

# à revoir 
class StrategieEncodage(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)

class TaxionomieTypeDonne(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)


class Encodage(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)

class Imputation(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)

class StrategieImputation(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)
    imputation = models.ForeignKey(Imputation, on_delete=models.CASCADE)
    taxionomie_type_tonne = models.ForeignKey(TaxionomieTypeDonne, on_delete=models.CASCADE)

class MiseEchelle(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)


class StrategieMiseEchelle(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    description =  models.CharField(max_length=254, blank=True,null=True)
    taxionomie_type_tonne = models.ForeignKey(TaxionomieTypeDonne, on_delete=models.CASCADE)
    mise_echelle = models.ForeignKey(MiseEchelle, on_delete=models.CASCADE)
    

class Colonne(models.Model):
    libelle = models.CharField(max_length=254, blank=True,null=True)
    typedonnee =  models.CharField(max_length=254, blank=True,null=True)
    estcategoriel = models.BooleanField()
    esttaget  = models.BooleanField()
    estelectionne = models.BooleanField()
    partten = models.CharField(max_length=254, blank=True,null=True)
    jeu_donnees = models.ForeignKey(JeuDonnees, on_delete=models.CASCADE)
    strategie_encodage = models.ForeignKey(StrategieEncodage, on_delete=models.CASCADE)
    strategie_imputation = models.ForeignKey(StrategieImputation, on_delete=models.CASCADE)
    strategie_mise_echelle = models.ForeignKey(StrategieMiseEchelle, on_delete=models.CASCADE)

class HyperParametre(models.Model):
    valeur = models.CharField(max_length=254, blank=True,null=True)
    cle =  models.CharField(max_length=254, blank=True,null=True)
    typedonnee = models.ForeignKey(TaxionomieTypeDonne, on_delete=models.CASCADE)

# Create your models here.
