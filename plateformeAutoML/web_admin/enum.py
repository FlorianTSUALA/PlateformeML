from django.db import models
from enum import Enum

class NoNameChoice(Enum):
    def __repr__(self):
        return self.value
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class TypeDonnee(NoNameChoice):
    ENTIER = 'ENTIER'
    DECIMAL = 'DECIMAL'
    CAHINE_CARACTERE = 'CAHINE_CARACTERE'
    INTERVALLE = 'INTERVALLE'

class EtatPublication(NoNameChoice):
    EN_ATTENTE_VALIDATION = 'EN_ATTENTE_VALIDATION'
    PUBLIC = 'PUBLIC'
    PRIVE = 'PRIVE'

class TypeValeur(NoNameChoice):
    QUALITATIF = 'QUALITATIF'
    QUANTITATIF = 'QUANTITATIF'
    NUMERIC = 'NUMERIC'
