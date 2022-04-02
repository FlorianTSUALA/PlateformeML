"""

"""
import sklearn

MAPPING_TYPE = {
    'ENTIER': {
        'data': ['int8', 'int16', 'int32', 'int64', 'uint8', 'uint16', 'uint32', 'uint64'],
        'type': 'int64',
        'label': 'Entier',
    },
    'REEL': {
        'data': ['float16', 'float32', 'float64'],
        'type': 'float64',
        'label': 'Réel',
    },
    'timedelta': {
        'data': [],
        'type': 'timedelta',
        'label': 'Complexe',
    },
    'CHAINE': {
        'data': ['str', 'mixed'],
        'type': 'object',
        'label': 'Chaîne',
    },
    'BOOLEEN': {
        'data': ['bool',],
        'type': 'bool',
        'label': 'Booléen',
    },
    'DATE': {
        'data': [],
        'type': 'datetime64',
        'label': 'Date',
    },
    'CATEGORY': {
        'data': [],
        'type': 'datetime64',
        'label': 'Date',
    },
}

MAPPING_SCALLER = {
    'StandardScaler': {
        'class': sklearn.preprocessing.StandardScaler(),
        'label':  'Standard Scaller',
        'parameter': ''
    },
    'MinMaxScaler': {
        'class':  sklearn.preprocessing.MinMaxScaler(),
        'label':  'Min Max Scaler',
        'parameter': ''
    },
    'RobustScaler': {
        'class': sklearn.preprocessing.RobustScaler(),
        'label':  'Robust Scaler',
        'parameter': ''
    },
    'MaxAbsScaler': {
        'class':sklearn.preprocessing.MaxAbsScaler(),
        'label':  'Max Abs Scaler',
        'parameter': ''
    },
}

MAPPING_IMPUTER = {

    'mean': {
        'class':'mean',
        'label':  'Moyenne',
    },
    'median': {
            'class':'median',
            'label':  'Median',
        },
    'most_frequent': {
            'class':'most_frequent',
            'label':  'valeur frequent',
        },
}

MAPPING_ENCODAGE = {
    'OneHotEncoder': {
        'class': sklearn.preprocessing.OneHotEncoder(),
        'label':  'OneHot Encoder',
    },
    'LabelEncoder': {
        'class': sklearn.preprocessing.LabelEncoder(),
        'label': 'Label Encoder',
    },
    'OrdinalEncoder': {
        'class': sklearn.preprocessing.OrdinalEncoder(),
        'label': 'OrdinalEncoder',
    },
}



"""
MAPPING_ENCODER = {
    "OneHotEncoder" : sklearn.preprocessing.OneHotEncoder,
    "OrdinalEncoder" : sklearn.preprocessing.OrdinalEncoder,
    "LabelEncoder" : sklearn.preprocessing.LabelEncoder,
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
"""