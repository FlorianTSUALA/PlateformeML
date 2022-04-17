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
    
def get_tache(default = False):
    collection  = ALGORITHME_SYSTEME
    data = dict()
    for key, value in collection.items():
        if data.get(value['task'], None) is None:
            data[value['task']] = list()      
        data[value['task']].append({'key':value['code'], 'value':value['label'], 'type_apprentissage': value['type_apprentissage']})
    if default:
        return data
    else:
        return data.keys()
    
def get_type_apprentissage(default = False):
    collection  = ALGORITHME_SYSTEME
    data = dict()
    
    for key, value in collection.items():
        if data.get(value['type_apprentissage'], None) is None:
            data[value['type_apprentissage']] = set()
        data[value['type_apprentissage']].add(value['task'])
    for key, value in data.items():
        data[key] = list(value)
        
    if default:
        return data
    else:
        return data.keys()

def get_package(default = False):
    collection  = ALGORITHME_SYSTEME
    data = dict()
    for key, value in collection.items():
        if data.get(value['package'], None) is None:
            data[value['package']] = list()      
        data[value['package']].append({key:value['code'], value:value['label']})
    if default:
        return data
    else:
        return data.keys()

    
def get_famille(default = False):
    collection  = ALGORITHME_SYSTEME
    data = dict()
    for key, value in collection.items():
        if data.get(value['family'], None) is None:
            data[value['family']] = list()      
        data[value['family']].append({'key':value['code'], 'value':value['label']})
    if default:
        return data
    else:
        return data.keys()

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