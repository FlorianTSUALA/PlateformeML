#from RModelFramework import DataImport
#from RModelFramework import PreprocessingData
#from  RModelFramework import Scoring
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from  ressources.resources import *

from refractoryFramwork.importation import  DataImport
from refractoryFramwork.pretraitement import PreprocessingData
#from refractoryFramwork.scoring import Scoring
from refractoryFramwork.classification.estimator import Estimator
if __name__ == "__main__":
    #pd.set_option('display.max_columns', None)

    data = DataImport(source)
    data.chargement()
    data.display_data(20)


    #target = 'Loan_Status'
    # dataset = data.delete_data_entry("Loan_ID",axis=1)


    target = "Churn"
    dataset = data.delete_data_entry("customerID", axis=1)

    print(dataset.columns)
    preprocessor1 = PreprocessingData(dataset,target,strategy_val_manquante_num='mean',methode_normalisation=StandardScaler(), strategy_val_manquante_cat='most_frequent',methode_encodage=OneHotEncoder())

    preprocessor1.encodage_label()

    ##donnee transformees

    data_traiter = preprocessor1.transfom()

    print("REPRESENTATION DES DONNEES PRETRAITER")
    print(data_traiter)

    dataset = preprocessor1.dataFrame

    print(dataset.head(20))

    preprocessor = preprocessor1.pipelinePreprocessing()


    ###################### INITIALISATION DES Algorithmes NECESSAIRES POUR LE SCORING #################


    Algorithmechoisis = ["RandomForest","AdaBoost","Binary_tree","KNN","LDA","Logistic"]

    dict_algo_choisis = {}
    for algo in Algorithmechoisis:
        initialisation_algo = list_of_model_disponible[algo][0]
        hyperparametre_algo = list_of_model_disponible[algo][1]
        pipeline_algo = make_pipeline(preprocessor,initialisation_algo)
        dict_algo_choisis[algo] = [pipeline_algo,hyperparametre_algo]



    classement = Estimator(dict_algo_choisis,dataset,target)
    #classement = Estimator(list_of_model, dataset, target)

    #pair_plot = scoring.matrix_corelation()

    #print(pair_plot)

    performences_models,best_model = classement.executer()

    print("la performence de tous les models  : ",performences_models)
    print("Le meilleur model est models:",best_model)

    classement.optimisationHyperParam()

    classement.save_model()

    classement.importance_features()

    #score_dataFrame = classement.scoring()
    #====================SCORING SUR DE NOUVEAU DONNEES ======================"=====


    class_dataFrame = classement.do_classification(df_new_scustomer)

    print(class_dataFrame)
