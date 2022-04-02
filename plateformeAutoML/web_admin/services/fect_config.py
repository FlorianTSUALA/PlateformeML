#from ..models import Algorithme
from plateformeAutoML.core_automl.bibliotheque.RMFrameClasse.ressources.mapping import *
from plateformeAutoML.core_automl.bibliotheque.RMFrameClasse.ressources.algorithme import *


class FecthConfigService():
    """
        Recuperation des entité
    """

    def encodage(self):

        liste_encodage = {}

        mapping_encoder = MAPPING_ENCODAGE

        for encodage  in mapping_encoder:
            nom = encodage
            label = mapping_encoder[encodage]['label']
            liste_encodage[encodage] = label

        return liste_encodage


    def imputation(self):

        liste_imputation = []

        mapping_imputer = MAPPING_IMPUTER

        for imputer in mapping_imputer:

            nom = imputer
            label = mapping_imputer[nom]['label']
            liste_imputation[imputer] = label

        return liste_imputation

    def mise_echelle(self):

        liste_scaller = []

        mapping_scallerr = MAPPING_SCALLER

        for scaller in mapping_scallerr:

            nom = scaller

            label = mapping_scallerr[scaller]['label']

            liste_scaller[nom] = label

        return liste_scaller

    def taxonomie_type_donnee(self):
        return 

    def strategie_encodage(self):
        return 

    def strategie_imputation(self):
        return 

    def strategie_mise_echelle(self):
        return 

    def famille(self):
        return 

    def tache(self):
        return 

    def type_apprentissage(self):
        return 

    def package(self):
        return 

    def algorithme(self):

        dict_algorithmes = {}

        algorithmes  = algorithmes_disponible

        for algo in algorithmes:

            nom = algo
            label = algorithmes[algo]['label']
            dict_algorithmes[nom] = label

        return dict_algorithmes

    def critere_comparaison(self):
        return 

    def critere_comparison_algorithme(self):
        return 

    def metrique(self):
        return 

    def metrique_algorithme(self):
        return 

    def metrique_algorithme_projet(self):
        return


if __name__ == "__main__":
    algos = FecthConfigService()


    print(algos.encodage())