from web_admin.models import Algorithme, Imputation, MiseEchelle, Encodage
from web_admin.models import StrategieEncodage, StrategieMiseEchelle, StrategieImputation
from web_admin.models import Famille, TaxonomieTypeDonnee
from .fetch_config import (get_algorithme, get_encodage, get_imputation, get_mise_echelle, get_taxonomie_type_donnee)

class ConfigManager():
    """
        Initialisaition des configurations natives du systeme au niveau 
        #todo
        check code if code don't exist create with generic mode | update
    """
    
def reset():
    pass

def clean():
    pass

##1
def algorithme(force = False):
    if force:
        Algorithme.objects.all().delete()
    if len(Algorithme.objects.all()) == 0:
        items = get_algorithme(True)
        for key in items:
            item = items[key]
            model = Algorithme(code = key, libelle = item['label'])

            model.save()
#3
def encodage(force = False):
    if force:
        Encodage.objects.all().delete()
    if len(Encodage.objects.all()) == 0:
        items = get_encodage(True)
        for key in items:
            item = items[key]
            model = Encodage(code = key, libelle = item['label'])
            model.save()
#3 
def imputation(force = False):
    if force:
        Imputation.objects.all().delete()
    if len(Imputation.objects.all()) == 0:
        items = get_imputation(True)
        for key in items:
            item = items[key]
            model = Imputation(code = key, libelle = item['label'])
            model.save()
#2
def mise_echelle(force = False):
    if force:
        MiseEchelle.objects.all().delete()
    if len(MiseEchelle.objects.all()) == 0:
        items = get_mise_echelle(True)
        for key in items:
            item = items[key]
            model = MiseEchelle(code = key, libelle = item['label'])
            model.save()
#1
def taxonomie_type_donnee(force = False):
    if force:
        TaxonomieTypeDonnee.objects.all().delete()
    if len(TaxonomieTypeDonnee.objects.all()) == 0:  
        items = get_taxonomie_type_donnee(True)
        for key in items:
            item = items[key]
            model = TaxonomieTypeDonnee(code = item['type'], libelle = item['label'], description = item['data'])
            model.save()
     
def strategie_encodage(force = False):
    if force:
        StrategieEncodage.objects.all().delete()
    if len(StrategieEncodage.objects.all()) == 0:
        taxonomie_type_donnee()
        for item in TaxonomieTypeDonnee.objects.all():
            model = StrategieEncodage(taxonomie_type_donnee=item)
            model.save()


def strategie_imputation(force = False):
    if force:
        StrategieImputation.objects.all().delete()
    if len(StrategieImputation.objects.all()) == 0: 
        taxonomie_type_donnee()
        for item in TaxonomieTypeDonnee.objects.all():
            model = StrategieImputation(taxonomie_type_donnee=item)
            model.save()
            print('ok')
        print('NOOH')

def strategie_mise_echelle(force = False):
    if force:
        StrategieMiseEchelle.objects.all().delete()
    if len(StrategieMiseEchelle.objects.all()) == 0: 
        taxonomie_type_donnee()
        for item in TaxonomieTypeDonnee.objects.all():
            model = StrategieMiseEchelle(taxonomie_type_donnee=item)
            model.save()

def famille(force = False):
    return 

def tache(force = False):
    return 

def type_apprentissage(force = False):
    return 

def package(force = False):
    return 

def critere_comparaison(force = False):
    return 

def critere_comparison_algorithme(force = False):
    return 

def metrique(force = False):
    return 

def metrique_algorithme(force = False):
    return 

def metrique_algorithme_projet(force = False):
    return  

def init():
    encodage()
    imputation()
    mise_echelle()
    taxonomie_type_donnee()
    # strategie_encodage()
    # strategie_imputation()
    # strategie_mise_echelle()
    # famille()
    # tache()
    # type_apprentissage()
    # package()
    # algorithme()
    # critere_comparaison()
    # critere_comparison_algorithme()
    # metrique()
    # metrique_algorithme()
    metrique_algorithme_projet()

if __name__ == "__main__":
    # sys_config = FecthConfigService()
    # print(sys_config.encodage())
    algorithme()
    print("algorithme()")
