
class AlgorithmeService:

    def __init__(self,libelle,description,hyperparametre):
        self.libelle = libelle
        self.description = description
        self.hyperametre = hyperparametre

    def get_libelle(self):
        return self.libelle

    def get_description(self):
        return self.description

    def get_hyerametre(self):
        return self.hyperametre

    def get_dict(self):

        key = self.libelle

        valeurs = self.hyperametre

        dict_algo = {key:valeurs}

        return dict_algo


    def add(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass



class Hyperametre:

    def __init__(self,libelle,liste_valeur):
        self.libelle = libelle
        self.liste_valeur = liste_valeur

    def get_libelle(self):
        return self.libelle

    def get_liste_valeur(self):
        return self.liste_valeur


    def get_dictHyperametre(self):

        return {self.libelle: self.liste_valeur}

    def add(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class Tache:

    def __init__(self, libelle,description):
        self.libelle = libelle
        self.desciption =  description

    def get_libelle(self):
        return self.libelle

    def get_description(self):
        return self.desciption


class Type_apprentissage:
    def __init__(self, libelle,description):
        self.libelle = libelle
        self.desciption =  description

    def get_libelle(self):
        return self.libelle

    def get_description(self):
        return self.desciption

    def add(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


















