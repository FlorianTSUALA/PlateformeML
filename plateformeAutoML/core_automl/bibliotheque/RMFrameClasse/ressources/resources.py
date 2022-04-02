# ===============================================================================
import sklearn.preprocessing
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import tree
from sklearn.pipeline import make_pipeline
import pandas as pd


hyper_params_svm = {
    'svc__gamma': [1e-3, 1e-4],
    'svc__C': [1, 10, 100, 1000],
    'pipeline__polynomialfeatures__degree': [2, 3, 4],
    'pipeline__selectkbest__k': range(4, 100)
}
hyper_params_logistic = {
    'logisticregression__penalty': ['l1', 'l2'],
    'logisticregression__C': [1, 10, 100, 1000],
    'pipeline__polynomialfeatures__degree': [2, 3, 4],
    'pipeline__selectkbest__k': range(4, 100)
}
hyper_params_knn = {}

hyper_params_radomForest = {}

hyper_params_MLP = {}

hyper_params_AdaBoost = {}

hyper_params_lda = {
    'lda__solver' : ['svd', 'lsqr', 'eigen'],
    'lda__shrinkage' : ['auto','float'] ,
    'pipeline__polynomialfeatures__degree': [2, 3, 4],
    'pipeline__selectkbest__k': range(4, 100)
}

hyper_params_tree = {
    'pipeline__polynomialfeatures__degree': [2, 3, 4],
    'pipeline__selectkbest__k': range(4, 100)
}

name_of_model = {
    "RandomForest":"Random Forest",
    "AdaBoost": "Ada Boost",
    "SVM": "Suport Vector Machine",
    "KNN": "K-Nearest Neighbor",
    "Logistic": " Logistic Regression",
    "MLP": "Multi layer Perceptron",
    "LDA": "Linear discriminant analysis",
    "Binary_tree": "Binary Tree"
}

model_initialisation = {
    "RandomForest" : RandomForestClassifier(random_state=0),
    "AdaBoost":  AdaBoostClassifier(random_state=0),
    "SVM": SVC(random_state=0),
    "KNN": KNeighborsClassifier(),
    "Logistic": LogisticRegression(random_state=0),
    "MLP":  MLPClassifier(),
    "LDA": LinearDiscriminantAnalysis(),
    "Binary_tree":  tree.DecisionTreeClassifier()
}

list_of_model_disponible = {
    "RandomForest" : [RandomForestClassifier(random_state=0),hyper_params_radomForest],
    "AdaBoost":  [AdaBoostClassifier(random_state=0),hyper_params_AdaBoost],
    "SVM": [SVC(random_state=0),hyper_params_svm],
    "KNN": [KNeighborsClassifier(),hyper_params_knn],
    "Logistic":[LogisticRegression(random_state=0),hyper_params_logistic],
    "MLP":  [MLPClassifier(),hyper_params_MLP],
    "LDA": [LinearDiscriminantAnalysis(),hyper_params_lda],
    "Binary_tree": [tree.DecisionTreeClassifier(),hyper_params_tree]
}


list_technique_imputation = {
    'mean' : "mean",
    "median" : "median",
    "most_frequent" : "most_frequent"
}

list_technique_normalisation = {
    "StandardScaler" : sklearn.preprocessing.StandardScaler,
    "MinMaxScaler" : sklearn.preprocessing.MinMaxScaler,
    "RobustScaler" : sklearn.preprocessing.RobustScaler,
    "MaxAbsScaler" : sklearn.preprocessing.MaxAbsScaler
}

list_technique_encodage= {
    "OneHotEncoder" : sklearn.preprocessing.OneHotEncoder,
    "OrdinalEncoder" : sklearn.preprocessing.OrdinalEncoder,
    "LabelEncoder" : sklearn.preprocessing.LabelEncoder,
}


##===================LIEN DU FICHIER DE TEST====================#
#source2 = r'train_u6lujuX_CVtuZ9i.csv'
source = r'C:\Users\USER\Documents\ML\PlateformeML\plateformeAutoML\core_automl\bibliotheque\RMFrameClasse\ressources\chunk.csv'

##==================New dataset customer ========================
#new_dataset = r'new_customers.csv'

#df_new = pd.read_csv(new_dataset)
#df_new_scustomer = df_new.drop(['Churn'], axis=1)
