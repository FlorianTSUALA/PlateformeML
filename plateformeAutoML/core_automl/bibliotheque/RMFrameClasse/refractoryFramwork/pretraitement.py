##=================== CLASSE  DE PRETRAITEMENT DES DONNEES ====================#
from pyexpat import model
from .aquisition import *

class PreprocessingData(Acquisision):

    def __init__(self,dataset,target,strategy_val_manquante_num='mean',methode_normalisation=StandardScaler(), strategy_val_manquante_cat='most_frequent',methode_encodage=OneHotEncoder()):
        super().__init__(dataset,target)
        self.numerical_features = self.apply_separation_data(self.dataFrame)[0]
        self.categorical_features = self.apply_separation_data(self.dataFrame)[1]
        #tech pretraitement
        self.strategy_val_manquante_num= strategy_val_manquante_num
        self.methode_normalisation=methode_normalisation
        self.strategy_val_manquante_cat = strategy_val_manquante_cat
        self.methode_encodage = methode_encodage
        #self.liste_colonnes = liste_colonnes

    def preprocessingVariableNumerique(self):
        numerical_pipeline = make_pipeline(SimpleImputer(strategy=self.strategy_val_manquante_num), self.methode_normalisation)
        return numerical_pipeline

    ##Fonction de pretraitement de variables un a un avec leurs techniques
    ##Respectives 
    def preprocessinVariable2(self):
        
        """Fonction de pretraitement de variables un a un avec leurs techniques
        Respectives """

        #colonnesObj  = self.liste_colonnes
        colonnesObj  = ""

        tuple_variable_transfrom = ()
        for var in colonnesObj:
            if var.est_target == False:
                nom_var = colonnesObj.libelle
                imputation = colonnesObj.imputation
                encodage = colonnesObj.encodage
                normalisation = colonnesObj.normalisation
                type_variable = colonnesObj.type_donnees
                if encodage!='':
                    variable_prepropressing = make_pipeline(
                        SimpleImputer(strategy = imputation), 
                        encodage)
                elif normalisation!='':
                    variable_prepropressing = make_pipeline(
                        SimpleImputer(strategy = imputation), 
                        normalisation)
                elif type_variable in ['ENTIER','DECIMAL']:
                     variable_prepropressing = make_pipeline(
                        SimpleImputer(strategy = "mean"), 
                        StandardScaler())
                else:
                      variable_prepropressing = make_pipeline(
                        SimpleImputer(strategy = "most_frequent"), 
                        OneHotEncoder())

                variable_transfrom = (variable_prepropressing,[var])
                l = list(tuple_variable_transfrom)
                l.append(variable_prepropressing)
                tuple_variable_transfrom = tuple(l)
        
        preprocessorVar = make_column_transformer(tuple_variable_transfrom)

        return preprocessorVar

        

    ## strategie de prétraitement des valeurs  catégorielles
    def preprocessingVariableCategoriel(self):
        categoriel_pipeline = make_pipeline(SimpleImputer(strategy=self.strategy_val_manquante_cat), self.methode_encodage)
        return categoriel_pipeline

    ##  appliquer le strategie sur les variables
    def preprocessingVariable(self, numerical_features, categorical_features):
        preprocessingVariableNumerique1 = self.preprocessingVariableNumerique()

        preprocessingVariableCategoriel1 = self.preprocessingVariableCategoriel()

        preprocessorVar = make_column_transformer((preprocessingVariableNumerique1, numerical_features),
                                                  (preprocessingVariableCategoriel1, categorical_features), remainder='passthrough'
                                                  )

        return preprocessorVar
    ## Pipeline final de prétraitement des données (include polynomial features and select best Variables)
    def pipelinePreprocessing(self, methode_selection_variable=SelectKBest(f_classif, k=10)):

        preprocessingVariable1 = self.preprocessingVariable(self.numerical_features, self.categorical_features)
        
        """Traitement de varaibles un à un"""
        #preprocessingVariable2 = self.preprocessinVariable2()

        self.pipeline_preprocessing = make_pipeline(preprocessingVariable1, PolynomialFeatures(2, include_bias=False),
                                     methode_selection_variable)
        return self.pipeline_preprocessing

    def transfom(self):
        self.encodage_label()
        train,test = self.train_test_set()
        X_train,y_train = train
        #print(X_train,y_train)
        self.pipelinePreprocessing(methode_selection_variable=SelectKBest(f_classif, k=10))
        pipeline_fit_transform = self.pipeline_preprocessing.fit_transform(X_train, y_train)
        self.df_transformed =  pd.DataFrame(pipeline_fit_transform)
        return pipeline_fit_transform, self.df_transformed