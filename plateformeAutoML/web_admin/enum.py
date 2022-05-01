from django.db import models
from enum import Enum

class ENoNameChoice(Enum):
    def __repr__(self):
        return self.value
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name.lower().replace('_', ' ')) for key in cls]

class ETypeDonnee(ENoNameChoice):
    ENTIER = 'ENTIER'
    DECIMAL = 'DECIMAL'
    REEL = 'REEL'
    CAHINE_CARACTERE = 'CAHINE_CARACTERE'
    INTERVALLE = 'INTERVALLE'

class EDype(ENoNameChoice):
    ENTIER = 'ENTIER'
    DECIMAL = 'DECIMAL'
    RELL = 'RELL'
    CAHINE_CARACTERE = 'CAHINE_CARACTERE'
    INTERVALLE = 'INTERVALLE'

class EEtatPublication(ENoNameChoice):
    EN_ATTENTE_VALIDATION = 'EN_ATTENTE_VALIDATION'
    PUBLIC = 'PUBLIC'
    PRIVE = 'PRIVE'

class ENatureValeur(ENoNameChoice):
    QUALITATIF = 'CATEGORIEL' #QUALITATIF DISCRET OU AUTRE...
    QUANTITATIF = 'QUANTITATIF' #DISCRET | CONTINUE 
    # NUMERIC = 'NUMERIC'

class EEtatCompte(ENoNameChoice):
    ARCHIVE = 'ARCHIVE'
    EN_ATTENTE_VALIDATION = 'EN_ATTENTE_VALIDATION'
    ACTIF = 'ACTIF'
