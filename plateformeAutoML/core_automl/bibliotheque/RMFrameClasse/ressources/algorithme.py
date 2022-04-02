from resources import *

algorithmes_disponible = {

    "RandomForest" : {
        'init' : RandomForestClassifier(random_state=0),
        'hyperparametre':hyper_params_radomForest,
        'label': "Random Forest"
    },
    "AdaBoost" : {
            'init' : AdaBoostClassifier(random_state=0),
            'hyperparametre': hyper_params_AdaBoost,
            'label': "Ada Booster"
        },
    "SVM" : {
            'init' : SVC(random_state=0),
            'hyperparametre':hyper_params_svm,
            'label': "Support Vactor Machine"
        },
    "KNN" : {
            'init' : KNeighborsClassifier(),
            'hyperparametre':hyper_params_knn,
            'label': "K-Nearest Neighbor"
        },
    "Logistic": {
        'init': LogisticRegression(random_state=0),
        'hyperparametre': hyper_params_knn,
        'label': "Logistic Regression"
    },
    "MLP": {
        'init': MLPClassifier(),
        'hyperparametre': hyper_params_MLP,
        'label': "Multi layer Perceptron"
    },
    "LDA": {
        'init': LinearDiscriminantAnalysis(),
        'hyperparametre': hyper_params_lda,
        'label': "Linear discriminant analysis"
    },
    "Binary_tree": {
        'init': tree.DecisionTreeClassifier(),
        'hyperparametre': hyper_params_tree,
        'label': "Binary Tree"
    },
}
