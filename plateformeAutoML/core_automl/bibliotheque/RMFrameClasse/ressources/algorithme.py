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
        'task': 'SUPERVISED',
        'family': 'CLASSIFICATION',
        'package': '',
    },
    'AdaBoost' : {
            'code': 'AdaBoost',
            'init' : AdaBoostClassifier(random_state=0),
            'hyperparametre': HYPER_PARAMETRE_ADABOOST,
            'label': 'Ada Booster',
            'task': 'SUPERVISED',
            'family': 'CLASSIFICATION',
            'package': '',
        },
    'SVM' : {
            'code': 'SVM',
            'init' : SVC(random_state=0),
            'hyperparametre': HYPER_PARAMETRE_SVM,
            'label': 'Support Vactor Machine',
            'task': 'SUPERVISED',
            'family': 'CLASSIFICATION',
            'package': '',
        },
    'KNN' : {
            'code': 'KNN',
                'init' : KNeighborsClassifier(),
            'hyperparametre': HYPER_PARAMETRE_KNN,
            'label': 'K-Nearest Neighbor',
            'task': 'SUPERVISED',
            'family': 'CLASSIFICATION',
            'package': '',
        },
    'Logistic': {
        'code': 'Logistic',
        'init': LogisticRegression(random_state=0),
        'hyperparametre': HYPER_PARAMETRE_KNN,
        'label': 'Logistic Regression',
        'task': 'REGRESSION',
        'family': 'CLASSIFICATION',
        'package': '',
    },
    'MLP': {
        'code': 'MLP',
        'init': MLPClassifier(),
        'hyperparametre': HYPER_PARAMETRE_MLP,
        'label': 'Multi layer Perceptron',
        'task': 'SUPERVISED',
        'family': 'CLASSIFICATION',
        'package': '',
    },
    'LDA': {
        'code': 'LDA',
        'init': LinearDiscriminantAnalysis(),
        'hyperparametre': HYPER_PARAMETRE_LDA,
        'label': 'Linear discriminant analysis',
        'task': 'SUPERVISED',
        'family': 'CLASSIFICATION',
        'package': '',
    },
    'Binary_tree': {
        'code': 'Binary_tree',
        'init': tree.DecisionTreeClassifier(),
        'hyperparametre': HYPER_PARAMETRE_TREE,
        'label': 'Binary Tree',
        'task': 'SUPERVISED',
        'family': 'CLASSIFICATION',
        'package': '',
    },
}
