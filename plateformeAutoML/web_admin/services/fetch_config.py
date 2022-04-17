from core_automl.bibliotheque.RMFrameClasse.ressources.mapping import (MAPPING_NATURE_VALEUR, MAPPING_TYPE, MAPPING_SCALLER, MAPPING_IMPUTER, MAPPING_ENCODER)
from core_automl.bibliotheque.RMFrameClasse.ressources.algorithme import (ALGORITHME_SYSTEME)


def get(default, collection):
    if default:
        return collection
    else:
        return dict((tag, collection[tag]['label']) for tag in collection)

def get_encodage(default = False):
     return get(default, MAPPING_ENCODER)

def get_imputation(default = False):
    return get(default, MAPPING_IMPUTER)

def get_mise_echelle(default = False):
    return get(default, MAPPING_SCALLER)
    
def get_algorithme(default = False):
    collection  = ALGORITHME_SYSTEME
    if default:
        return collection
    else:
        return dict((tag, collection[tag]['label']) for tag in collection)
        
    
def get_allgorithme_by_task(task):
    collection  = ALGORITHME_SYSTEME
    return dict((key, value['label']) for key, value in collection if value['task'] == str(task))
        
def get_nature_valeur(default = False):
    collection  = MAPPING_NATURE_VALEUR
    if default:
        return collection
    else:
        return dict((collection[tag]['type'], collection[tag]['label']) for tag in collection)
        
def get_taxonomie_type_donnee(default = False):
    collection  = MAPPING_TYPE
    if default:
        return collection
    else:
        return dict((tag, collection[tag]['label']) for tag in collection)

def get_strategie_encodage(self):
    return 

def get_strategie_imputation(self):
    return 

def get_strategie_mise_echelle(self):
    return 

def get_famille(self):
    return 

def get_tache(self):
    return 

def get_type_apprentissage(self):
    return 

def get_package(self):
    return 

def get_critere_comparaison(self):
    return 

def get_critere_comparison_algorithme(self):
    return 

def get_metrique(self):
    return 

def get_metrique_algorithme(self):
    return 

def get_metrique_algorithme_projet(self):
    return

def fecth(self):
    pass


class FecthConfigService():
    """
        Recuperation des entité
    """

if __name__ == "__main__":
    # sys_config = FecthConfigService()
    # print(sys_config.encodage())
    print(encodage())

"""
        liste_encodage = {}
        MAPPING_ENCODAGE = MAPPING_ENCODAGE
        for encodage  in MAPPING_ENCODAGE:
            nom = encodage
            label = MAPPING_ENCODAGE[encodage]['label']
            liste_encodage[encodage] = label

        return liste_encodage
"""