##===================CLASSE ABSTRAITE DES FONCTIONS APPLICABLES SUR  UN MODEL====================#
import pickle
from pathlib import Path

from .pretraitement import *

##===================BIBLIOTHEQUE POUR POUR LA MESURE DE PERFORMENCE DU MODEL L'OPTIMISATION DES HYPERPARAMETRES
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import f1_score, confusion_matrix, classification_report
#from sklearn.model_selection import learning_curve
from sklearn.metrics import accuracy_score

import  seaborn as sns

##===================BIBLIO CLASSE ABSTRAITE
from abc import ABC, abstractmethod

class IModel:
    @abstractmethod
    def evaluerModel(self):
        pass

    @abstractmethod
    def evalModels(self):
        pass

    @abstractmethod
    def compareModels(self):
        pass

    @abstractmethod
    def rapport(self, data):
        pass

    @abstractmethod
    def  optimisationHyperParam(self,data):
        pass

    @abstractmethod
    def predire(self, data):
        pass

    @abstractmethod
    def save_model(self):
        pass


    @classmethod
    def save_model(cls,model, path,num):
        try:
            filename = path+"/"+str(num)+".sav"
            Path(filename).parent.mkdir(exist_ok=True, parents=True)
            pickle.dump(model, open(filename,'wb'))
            return filename
        except Exception as e:
            print('Failled to save model')
            print('-'*60)
            print(e)
            print('-'*60)
            return 0
    
    @classmethod
    def load_model(cls,filename):
        try:
            return pickle.load(open(filename, 'rb'))
        except Exception as e:
            print('Failled to load model')
            print('-'*60)
            print(e)
            print('-'*60)
            return 0

class RMFrammeEstimator(IModel,PreprocessingData):

    def __init__(self, listeModel,dataset,target):

        super().__init__(dataset, target)

        train_set, test_set = self.train_test_set()
        self.models = listeModel
        self.best_model = ''
        self.X_train = train_set[0]
        self.y_train = train_set[1]
        self.X_test = test_set[0]
        self.y_test = test_set[1]
        self.model_save = ''
        self.new_dataFrame = ''


    # PROCEDURE D'EVALUATION DES DIFFERRENTS MODELS
def feateares_encoding(df):
    """ Encodes data and returns new data """
    mask = df.dtypes==object
    #get_categorical()
    categorical = df.columns[mask].tolist()
    print(categorical)
    if categorical:
        #Encoder foreach column
        le = LabelEncoder()
        df[categorical] = df[categorical].apply(lambda x: le.fit_transform(x.astype(str)))
        # df.to_csv(path, index=False)
    return df


    # mesure = ['f1','precision','recall']
    def evaluerModel(self,model):
        base_model = model.fit(self.X_train, self.y_train)
        print("les données de test ::::::::::::::::::::",self.X_test)
        print("les données de test ::::::::::::::::::::",self.X_test.dtypes)
        y_pred = model.pred-ict(self.X_test)
        precision = accuracy_score(self.y_test, y_pred)
        return base_model,precision

    def rapport(self, model):
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        # print(confusion_matrix(y_test,y_pred))
        # report = print(classification_report(y_test,y_pred))
        report = classification_report(self.y_test, y_pred)
        return report

    def matrixConfusion(self, model):
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        # matrix = print(confusion_matrix(y_test,y_pred))
        matrix = confusion_matrix(self.y_test, y_pred)
        return matrix

    # Fonction qui prend en paramètre une liste de modèles prédéfinis et les variables test et entrainement
    # Puis renvoie un dictionnaire contenant tous les modèles ainsi que leurs scores respectifs

    def evalModels(self):
        precision_dico_models = {}
        precision_ = 0
        model_ = ""
        models_fit = {}
        for name, model in self.models.items():
            base_model,precision = self.evaluerModel(model[0])
            precision_dico_models[name] = precision
            models_fit[name] = [base_model,precision]

            if precision > precision_:
                precision_ = precision
                model_ = base_model
                name_ = name

        print("bonjourrrrrrrrrrrrrrrrrrrr",precision_)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxx",model_)

        #return precision_dico_models,model_,precision_
        return precision_dico_models,models_fit,precision_,name_

    # Fonction qui permet de faire la comparaison entre les modèles entrainés et retourne celui ayant la meilleure
    # performance.
    def compareModels(self, dictionnaire):
        best = 0
        model = ''
        for item, value in dictionnaire.items():
            if best < value:
                best = value
                model = item
        self.best_model = model
        return model, best

    # optimisation du modèle le plus performant
    def optimisationHyperParam(self,model, scoring='f1', cv=10):
        print(self.X_test)
        print(self.y_test)
        print(self.target)
        #model_algo = self.best_model
        model_algo = model
        print("----------xx--------",model_algo)
        grid = RandomizedSearchCV(self.models[model_algo][0], self.models[model_algo][1], scoring=scoring, cv=cv, n_iter=100)

        #grid = GridSearchCV(self.models[model_algo][0], self.models[model_algo][1], scoring=scoring, cv=cv,n_jobs=5, verbose=2)

        #model = grid.fit(self.X_train, self.y_train)
        #self.model_save = model

        base_model,precision = self.evaluerModel(grid)

        #y_pred = grid.predict(self.X_test)
        #print(classification_report(self.y_test, y_pred))

        return base_model,precision

    def rapport_analyse(self):
        y_pred = self.model_save.predict(self.X_test)
        print(classification_report(self.y_test, y_pred))
        return classification_report(self.y_test, y_pred)


    def get_save_model(self):
        return self.model_save


    def show_permences_model(self,dictionnaire):
        import matplotlib.pyplot as plt
        """data = {'Logistic Regression': acc_lr, 'KNN': acc_knn,
                'Support Vector Classifier': acc_svc, 'Decision Tree Classifier': acc_dtc,
                'Random Forest Classifier': acc_rf,
                'Ada Boost Classifier': acc_adc, 'Extra Trees Classifier': acc_etc,
                'Bagging Classifier': acc_bgc, 'Gradient Boosting Classifier': acc_gbc,
                'XGBoost Classifier': acc_xgbc}"""

        data = dict(sorted(dictionnaire.items(), key=lambda x: x[1], reverse=True))
        models = list(data.keys())
        score = list(data.values())
        fig = plt.figure(figsize=(15, 10))
        sns.barplot(x=score, y=models)
        plt.xlabel("Models Utilisés", size=20)
        plt.xticks(size=12)
        plt.ylabel("Score", size=20)
        plt.yticks(size=12)
        plt.title("Score des modèles non optimisés ", size=25)
        #plt.show()
        plt.savefig


    def importance_features(self):
        model_rf = self.model_save.best_estimator_._final_estimator
        X = self.X
        print(X.columns.values)
        #importances = model_rf.feature_importances_
        coef = model_rf.coef_[0]
        print(len(coef))
        weights = pd.Series(coef[:8],
                            index=X.columns.values)
        print(weights.sort_values()[-10:].plot(kind='barh'))


    """def executer(self):
        precision_dico_models,model_,precision_ = self.evalModels()
        self.show_permences_model(precision_dico_models)
        result = self.compareModels(precision_dico_models)
        return precision_dico_models,result,model_,precision_"""

    def executer(self):
        precision_dico_models, models_fit, precision_,name_ = self.evalModels()
        #precision_dico_models,models_fit= self.evalModels()
        #self.show_permences_model(precision_dico_models)
        #result = self.compareModels(precision_dico_models)
        return precision_dico_models,models_fit,precision_,name_

