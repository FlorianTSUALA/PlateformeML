
from core_automl.core_2.ressources.resources import *


from core_automl.core_2.refractoryFramwork.importation import  DataImport
from core_automl.core_2.refractoryFramwork.pretraitement import PreprocessingData



if __name__ == "__main__":

    """test des fonction de la bibliotheque"""

    """chargement des fichier csv"""
    source = r'chunk.csv'
    data = DataImport(source)
    data.chargement()

    """Affichage des 20 premieres ligne"""
    data.display_data(20)




    """suppression d'une colonne particulière"""
    dataset = data.delete_data_entry("customerID", axis=1)
    print(dataset.columns)

    target = "Churn"


    """TEST DE PRETRAITEMENT"""
    preprocessor1 = PreprocessingData(dataset,target)

    preprocessor1.encodage_label()

    dataset = preprocessor1.dataFrame

   


    preprocessor = preprocessor1.pipelinePreprocessing()


    print(preprocessor1.transfom())

    

    """


    ###################### INITIALISATION DES Algorithmes NECESSAIRES POUR LE SCORING #################

    RandomForest = make_pipeline(preprocessor, RandomForestClassifier(random_state=0))
    AdaBoost = make_pipeline(preprocessor, AdaBoostClassifier(random_state=0))
    SVM = make_pipeline(preprocessor, SVC(random_state=0))
    KNN = make_pipeline(preprocessor, KNeighborsClassifier())
    Logistic = make_pipeline(preprocessor, LogisticRegression(random_state=0))
    MLP = make_pipeline(preprocessor, MLPClassifier())
    LDA = make_pipeline(preprocessor,LinearDiscriminantAnalysis())
    Binary_tree = make_pipeline(preprocessor,tree.DecisionTreeClassifier())



    #####Dictionnaire des Algorithmes avec leurs hyperparamètres

    list_of_model = {
        "RandomForest": [RandomForest, hyper_params_radomForest],
        #"AdaBoost": [AdaBoost, hyper_params_AdaBoost],
        #"SVM": [SVM, hyper_params_svm],
        #"KNN": [KNN, hyper_params_knn],
        "Logistic": [Logistic, hyper_params_logistic],
        "MLP": [MLP, hyper_params_MLP],
        "LDA":[LDA,hyper_params_lda],
        "Binary_tree":[Binary_tree,hyper_params_tree]
    }

    scoring = Scoring(list_of_model,dataset,target)

    #pair_plot = scoring.matrix_corelation()

    #print(pair_plot)

    performences_models,best_model = scoring.executer()

    print("la performence de tous les models  : ",performences_models)
    print("Le meilleur model est models:",best_model)

    scoring.optimisationHyperParam()

    scoring.save_model()

    scoring.importance_features()

    score_dataFrame = scoring.scoring()
    #====================SCORING SUR DE NOUVEAU DONNEES ======================"=====


    score_dataFrame = scoring.scoring_new_data(df_new_scustomer)

    print(score_dataFrame)"""
