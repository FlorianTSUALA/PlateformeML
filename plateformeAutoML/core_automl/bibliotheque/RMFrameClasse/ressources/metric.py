from sklearn import metrics
#https://scikit-learn.org/stable/modules/classes.html#sklearn-metrics-metrics
METRICS = {
    'Accuracy':{
        'code': 'Accuracy',
        'label': 'Accuracy',
        'task': 'Classification',
        # 'package': metrics.accuracy_score,
    },
    'F1':{
        'code': 'F1',
        'label': 'F1 Score',
        'task': 'Classification',
        # 'package': metrics.f1_score,
    },
    'Precision':{
        'code': 'Precision',
        'label': 'Precision',
        'task': 'Classification',
        # 'package': metrics.precision_score,
    },
    'Recall':{
        'code': 'Recall',
        'label': 'Recall',
        'task': 'Classification',
        # 'package': metrics.recall_score,
    },
    'ROC_AUC':{
        'code': 'ROC_AUC',
        'label': 'ROC AUC',
        'task': 'Classification',
        # 'package': metrics.roc_auc_score,
    },
    'R2':{
        'code': 'R2',
        'label': 'R2',
        'task': 'Regression',
        # 'package': metrics.r2_score,
    },
    'Mean_Squared_Error':{
        'code': 'Mean_Squared_Error',
        'label': 'Mean Squared Error',
        'task': 'Regression',
        # 'package': metrics.mean_squared_error,
    },
    'Mean_Absolute_Error':{
        'code': 'Mean_Absolute_Error',
        'label': 'Mean Absolute Error',
        'task': 'Regression',
        # 'package': metrics.mean_absolute_error,
    },
    'Median_Absolute_Error':{
        'code': 'Median_Absolute_Error',
        'label': 'Median Absolute Error',
        'task': 'Regression',
        # 'package': metrics.median_absolute_error,
    },
}