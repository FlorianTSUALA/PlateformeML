from autosklearn import metrics
from sklearn.preprocessing import *
from sklearn.impute import *


CLASSIFIERS = [
    "adaboost",
    "bernoulli_nb",
    "decision_tree",
    "extra_trees",
    "gaussian_nb",
    "gradient_boosting",
    "k_nearest_neighbors",
    "lda",
    "liblinear_svc",
    "libsvm_svc",
    "multinomial_nb",
    "passive_aggressive",
    "qda",
    "random_forest",
    "sgd"
]

CLASSIFIERS_DISP = [
    "AdaBoost",
    "Bernoulli NB",
    "Decision Tree",
    "Extra Trees",
    "Gaussian NB",
    "Gradient Boosting",
    "K Nearest Neighbors",
    "LDA",
    "Liblinear SVC",
    "Libsvm SVC",
    "Multinomial NB",
    "Passive Aggressive",
    "QDA",
    "Random Forest",
    "SGD"
    ]

REGRESSORS = [
    "adaboost",
    "ard_regression",
    "decision_tree",
    "extra_trees",
    "gaussian_process",
    "gradient_boosting",
    "k_nearest_neighbors",
    "liblinear_svr",
    "libsvm_svr",
    "random_forest",
    "sgd",
    "xgradient_boosting"]

REGRESSORS_DISP = [
    "AdaBoost",
    "ARD",
    "Decision Tree",
    "Extra Trees",
    "Gaussian Process",
    "Gradient Boosting",
    "K Nearest Neighbors",
    "Liblinear SVR",
    "Libsvm SVR",
    "Random Forest",
    "SGD",
    "XGradient Boosting"]

PREPROCESSORS_CL = [
    "no_preprocessing",
    "extra_trees_preproc_for_classification",
    "fast_ica",
    "feature_agglomeration",
    "kernel_pca",
    "kitchen_sinks",
    "liblinear_svc_preprocessor",
    "nystroem_sampler",
    "pca",
    "polynomial",
    "random_trees_embedding",
    "select_percentile_classification",
    "select_percentile_regression",
    "select_rates",
    "truncatedSVD"]

PREPROCESSORS_CL_DISP = [
    "No Preprocessing",
    "Extra Trees Preprocessor",
    "Fast ICA",
    "Feature Agglomeration",
    "Kernel PCA",
    "Litchen Sinks",
    "Liblinear SVC Preprocessor",
    "Nystroem Sampler",
    "PCA",
    "Polynomial",
    "Random Trees Embedding",
    "Select Percentile Classification",
    "Select Percentile Regression",
    "Select Rates",
    "Truncated SVD"]

PREPROCESSORS_RG = [
    "no_preprocessing",
    "extra_trees_preproc_for_regression",
    "fast_ica",
    "feature_agglomeration",
    "kernel_pca",
    "kitchen_sinks",
    "liblinear_svc_preprocessor",
    "nystroem_sampler",
    "pca",
    "polynomial",
    "random_trees_embedding",
    "select_percentile_classification",
    "select_percentile_regression",
    "select_rates",
    "truncatedSVD"]

PREPROCESSORS_RG_DISP = [
    "No Preprocessing",
    "Extra Trees Preprocessor",
    "Fast ICA",
    "Feature Agglomeration",
    "Kernel PCA",
    "Kitchen Sinks",
    "Liblinear SVC Preprocessor",
    "Nystroem Sampler",
    "PCA",
    "Polynomial",
    "Random Trees Embedding",
    "Select Percentile Classification",
    "Select Percentile Regression",
    "Select Rates",
    "Truncated SVD"]

METRICS_CL = [
    metrics.accuracy,
    metrics.f1_macro,
    metrics.precision,
    metrics.recall,
    metrics.roc_auc]

METRICS_RG = [
    metrics.r2,
    metrics.mean_squared_error,
    metrics.mean_absolute_error,
    metrics.median_absolute_error
]

METRICS_CL_DISP = ["Accuracy", "F1", "Precision", "Recall", "ROC AUC"]

METRICS_RG_DISP = [
    "R2",
    "Mean Squared Error",
    "Mean Absolute Error",
    "Median Absolute Error"]

CLASSIFIERS = [
    "adaboost",
    "bernoulli_nb",
    "decision_tree",
    "extra_trees",
    "gaussian_nb",
    "gradient_boosting",
    "k_nearest_neighbors",
    "lda",
    "liblinear_svc",
    "libsvm_svc",
    "multinomial_nb",
    "passive_aggressive",
    "qda",
    "random_forest",
    "sgd"]

def gen_metric(task, metrics_choice):
    if task == "classification":
        return METRICS_CL[METRICS_CL_DISP.index(metrics_choice)]
    else:
        return METRICS_RG[METRICS_RG_DISP.index(metrics_choice)]


def format_ls(ls, val):
    if(ls == "cl"):
        rs = CLASSIFIERS_DISP[CLASSIFIERS.index(val)]
    elif(ls == "rg"):
        rs = REGRESSORS_DISP[REGRESSORS.index(val)]
    elif(ls == "cp"):
        rs = PREPROCESSORS_CL_DISP[PREPROCESSORS_CL.index(val)]
    elif(ls == "rp"):
        rs = PREPROCESSORS_RG_DISP[PREPROCESSORS_RG.index(val)]
    else:
        rs = "wrong argument"
    return rs



ENCODAGE = {
    "LabelEncoder":LabelEncoder(),
    "LabelBinarizer":LabelBinarizer(),
    "OneHotEncoder":OneHotEncoder(),
    "OrdinalEncoder":OrdinalEncoder(),
}

MISE_ECHELLE = {
    "StandardScaler": StandardScaler(),
    "MinMaxScaler": MinMaxScaler(),
    "RobustScaler" : RobustScaler(),
    "MaxAbsScaler" : MaxAbsScaler()
}
strategy = ["mean","median","max","min"]

n_neighbors = 5

IMPUTER = {
    SimpleImputer : strategy,
    KNNImputer : n_neighbors
}

STRATEGY = [
    "IMPUTATION",
    "ENCODAGE",
    "MISE A l'ECHELLE"
]


