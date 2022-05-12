from web_admin.models import Algorithme, Imputation, MiseEchelle, Encodage
from web_admin.models import StrategieEncodage, StrategieMiseEchelle, StrategieImputation
from web_admin.models import Famille, TaxonomieTypeDonnee, Package, TypeApprentissage, Metrique, Tache
from .fetch_config import (get_algorithme, get_encodage, get_imputation, get_mise_echelle, get_taxonomie_type_donnee)
from .fetch_config import (get_metrique, get_type_apprentissage, get_tache, get_package, get_famille)

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

#0a0
def type_apprentissage(force = False):
    if force:
        TypeApprentissage.objects.all().delete()
    if len(TypeApprentissage.objects.all()) == 0:
        items = get_type_apprentissage(True)
        for key in items:
            item = items[key]
            model = TypeApprentissage(code = key, libelle = item['label'])
            model.save() 
    
#0a1
def tache(force = False):
    type_apprentissage(force)
    if force:
        Tache.objects.all().delete()
    if len(Tache.objects.all()) == 0:
        items = get_tache(True)
        for key in items:
            item = items[key]
            _type_apprentissage = TypeApprentissage.objects.get(code=item['type_appretissage'])
            model = Tache(code = key, libelle = item['label'], type_apprentissage =_type_apprentissage)
            model.save()

#0a2
def metrique(force = False):
    tache(force)
    if force:
        Metrique.objects.all().delete()
    if len(Metrique.objects.all()) == 0:
        items = get_metrique(True)
        for key in items:
            item = items[key]
            _tache = Tache.objects.get(code=item['task'])
            model = Metrique(code = key, libelle = item['label'], tache = _tache)
            model.save()
#0
def package(force = False):
    if force:
        Package.objects.all().delete()
    if len(Package.objects.all()) == 0:
        items = get_package(True)
        data = set()
        for key in items:
            data.add(key)
        for key in data:
            model = Package(code = key, libelle = key)
            model.save()

#0
def famille(force = False):
    if force:
        Famille.objects.all().delete()
    if len(Famille.objects.all()) == 0:
        items = get_famille(True)
        for key in items:
            item = items[key]
            print(key, item)
            model = Famille(code = key, libelle = key)
            # model = Famille(code = key, libelle = item['label'])
            model.save()

##
def algorithme(force = False):
    if force:
        Algorithme.objects.all().delete()
    if len(Algorithme.objects.all()) == 0:
        items = get_algorithme(True)
        for key in items:
            item = items[key]
            model = Algorithme(code = key, libelle = item['label'])

            model.save()

#0
def encodage(force = False):
    if force:
        Encodage.objects.all().delete()
    if len(Encodage.objects.all()) == 0:
        items = get_encodage(True)
        for key in items:
            item = items[key]
            model = Encodage(code = key, libelle = item['label'])
            model.save()
#0 
def imputation(force = False):
    if force:
        Imputation.objects.all().delete()
    if len(Imputation.objects.all()) == 0:
        items = get_imputation(True)
        for key in items:
            item = items[key]
            model = Imputation(code = key, libelle = item['label'])
            model.save()
#0
def mise_echelle(force = False):
    if force:
        MiseEchelle.objects.all().delete()
    if len(MiseEchelle.objects.all()) == 0:
        items = get_mise_echelle(True)
        for key in items:
            item = items[key]
            model = MiseEchelle(code = key, libelle = item['label'])
            model.save()
#0
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


def critere_comparaison(force = False):
    return 

def critere_comparison_algorithme(force = False):
    return 


def run():
    type_apprentissage()
    tache()
    famille()
    metrique()
    package() 
    
    encodage()
    imputation()
    mise_echelle()
    
    taxonomie_type_donnee()
    algorithme()
    # metrique_algorithme()
    
    strategie_encodage()
    strategie_imputation()
    strategie_mise_echelle()
    
    # critere_comparaison()
    # critere_comparison_algorithme()

if __name__ == "__main__":
    # sys_config = FecthConfigService()
    # print(sys_config.encodage())
    algorithme()
    print("algorithme()")
