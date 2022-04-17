from sklearn import tree
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from .hyperparametre import *

ALGORITHME_SYSTEME = {

    'RandomForest' : {
        'code': 'RandomForest',
        'init' : RandomForestClassifier(random_state=0),
        'hyperparametre': HYPER_PARAMETRE_RADOMFOREST,
        'label': 'Random Forest',
        'metadata':{
            'tag': '',
        },
        'task': 'Classification',
        'type_apprentissage': 'Supervise',
        'family': 'Decision Tree',
        'package': 'scikit-learn',
    },
    'AdaBoost' : {
            'code': 'AdaBoost',
            'init' : AdaBoostClassifier(random_state=0),
            'hyperparametre': HYPER_PARAMETRE_ADABOOST,
            'label': 'Ada Booster',
            'metadata':{
                'tag': '',
            },
            'task': 'Classification',
            'type_apprentissage': 'Supervise',
            'implemented': True,
            'family': 'Ensemble',
            'package': 'scikit-learn',
        },
    'SVM' : {
            'code': 'SVM',
            'init' : SVC(random_state=0),
            'hyperparametre': HYPER_PARAMETRE_SVM,
            'label': 'Support Vactor Machine',
            'metadata':{
                'tag': '',
            },
            'task': 'Classification',
            'type_apprentissage': 'Supervise',
            'family': 'Nom linéaire',
            'package': 'scitki-learn',
        },
    'KNN' : {
            'code': 'KNN',
            'init' : KNeighborsClassifier(),
            'hyperparametre': HYPER_PARAMETRE_KNN,
            'label': 'K-Nearest Neighbor',
            'metadata':{
                'tag': '',
            },
            'task': 'Classification',
            'type_apprentissage': 'Supervise',
            'family': 'Nom linéaire',
            'package': 'scikit-learn',
        },
    'Logistic': {
        'code': 'Logistic',
        'init': LogisticRegression(random_state=0),
        'hyperparametre': HYPER_PARAMETRE_KNN,
        'label': 'Logistic Regression',
        'metadata':{
            'tag': '',
        },
        'task': 'Classification',
        'type_apprentissage': 'Supervise',
        'family': 'Lineaire',
        'package': 'scikit-learn',
    },
    'MLP': {
        'code': 'MLP',
        'init': MLPClassifier(),
        'hyperparametre': HYPER_PARAMETRE_MLP,
        'label': 'Multi layer Perceptron',
        'metadata':{
            'tag': '',
        },
        'task': 'Classification',
        'type_apprentissage': 'Supervise',
        'family': 'Non Lineaire',
        'package': 'scikit-learn',
    },
    'LDA': {
        'code': 'LDA',
        'init': LinearDiscriminantAnalysis(),
        'hyperparametre': HYPER_PARAMETRE_LDA,
        'label': 'Linear discriminant analysis',
        'metadata':{
            'tag': '',
        },
        'task': 'Classification',
        'type_apprentissage': 'Supervise',
        'family': 'Lineaire',
        'package': 'scikit-learn',
    },
    'Binary_tree': {
        'code': 'Binary_tree',
        'init': tree.DecisionTreeClassifier(),
        'hyperparametre': HYPER_PARAMETRE_TREE,
        'label': 'Binary Tree',
        'metadata':{
            'tag': '',
        },
        'task': 'Classification',
        'type_apprentissage': 'Supervise',
        'family': 'Decision Tree',
        'package': 'scikit-learn',
    },
}
