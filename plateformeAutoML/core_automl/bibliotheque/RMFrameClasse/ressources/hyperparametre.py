
HYPER_PARAMETRE_SVM = {
    'svc__gamma': [1e-3, 1e-4],
    'svc__C': [1, 10, 100, 1000],
    'pipeline__polynomialfeatures__degree': [2, 3, 4],
    'pipeline__selectkbest__k': range(4, 100)
}

HYPER_PARAMETRE_LOGISTIC = {
    'logisticregression__penalty': ['l1', 'l2'],
    'logisticregression__C': [1, 10, 100, 1000],
    'pipeline__polynomialfeatures__degree': [2, 3, 4],
    'pipeline__selectkbest__k': range(4, 100)
}

HYPER_PARAMETRE_KNN = {}

HYPER_PARAMETRE_RADOMFOREST = {}

HYPER_PARAMETRE_MLP = {}

HYPER_PARAMETRE_ADABOOST = {}

HYPER_PARAMETRE_LDA = {
    'lda__solver' : ['svd', 'lsqr', 'eigen'],
    'lda__shrinkage' : ['auto','float'] ,
    'pipeline__polynomialfeatures__degree': [2, 3, 4],
    'pipeline__selectkbest__k': range(4, 100)
}

HYPER_PARAMETRE_TREE = {
    'pipeline__polynomialfeatures__degree': [2, 3, 4],
    'pipeline__selectkbest__k': range(4, 100)
}
