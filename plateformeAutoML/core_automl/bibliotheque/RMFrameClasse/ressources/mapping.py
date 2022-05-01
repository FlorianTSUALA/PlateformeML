from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder
from sklearn.preprocessing import LabelEncoder, StandardScaler, RobustScaler, MinMaxScaler, MaxAbsScaler

MAPPING_NATURE_VALEUR = {
    'CATEGORIEL': {
        'data': [],
        'label': 'Catégoriel',
        'type': 'CATEGORIEL',
    },
    'QUATITATIF': {
        'data': [],
        'label': 'Quantitatif',
        'type': 'QUATITATIF',
    },
}

MAPPING_TYPE = {
    'ENTIER': {
        'data': ['int8', 'int16', 'int32', 'int64', 'uint8', 'uint16', 'uint32', 'uint64'],
        'type': 'int64',
        'label': 'Entier',
        'preprocessing': {
            'scaller': 'STANDARD_SCALER',
            'encoder': None,
            'imputer': 'MEAN',
        },
    },
    'REEL': {
        'data': ['float16', 'float32', 'float64'],
        'type': 'float64',
        'label': 'Réel',
        'preprocessing': {
            'scaller': 'STANDARD_SCALER',
            'encoder': None,
            'imputer': 'MEAN',
        },
    },
    'TIMEDELTA': {
        'data': [],
        'type': 'timedelta',
        'label': 'Complexe',
        'preprocessing': {
            'scaller': None,
            'encoder': None,
            'imputer': None,
        },
    },
    'CHAINE': {
        'data': ['str', 'mixed'],
        'type': 'object',
        'label': 'Chaîne',
        'preprocessing': {
            'scaller': None,
            'encoder': 'ONE_HOT_ENCODER',
            'imputer': 'MOST_FREQUENT',
        },
    },
    'BOOLEEN': {
        'data': ['bool',],
        'type': 'bool',
        'label': 'Booléen',
        'preprocessing': {
            'scaller': None,
            'encoder': 'ONE_HOT_ENCODER',
            'imputer': 'MOST_FREQUENT',
        },
    },
    'DATE': {
        'data': [],
        'type': 'datetime64',
        'label': 'Date',
        'preprocessing': {
            'scaller': None,
            'encoder': None,
            'imputer': None,
        },
    },
    'CATEGORY': {
        'data': [],
        'type': 'datetime64',
        'label': 'Date',
        'preprocessing': {
            'scaller': None,
            'encoder': None,
            'imputer': None,
        },
    },
}

MAPPING_SCALLER = {
    'STANDARD_SCALER': {
        'class': StandardScaler(),
        'label':  'Standard Scaller',
        'parameter': '', 
    },
    'MIN_MAX_SCALER': {
        'class':  MinMaxScaler(),
        'label':  'Min Max Scaler',
        'parameter': ''
    },
    'ROBUST_SCALER': {
        'class': RobustScaler(),
        'label':  'Robust Scaler',
        'parameter': ''
    },
    'MAX_ABS_SCALER': {
        'class':MaxAbsScaler(),
        'label':  'Max Abs Scaler',
        'parameter': ''
    },
}

MAPPING_IMPUTER = {
    'MEAN': {
        'class':'mean',
        'label':  'Moyenne',
    },
    'MEDIAN': {
            'class':'median',
            'label':  'Median',
    },
    'MOST_FREQUENT': {
            'class':'most_frequent',
            'label':  'valeur frequent',
    },
}

MAPPING_ENCODER = {
    'ONE_HOT_ENCODER': {
        'class': OneHotEncoder(),
        'label':  'OneHot Encoder',
    },
    'LABEL_ENCODER': {
        'class': LabelEncoder(),
        'label': 'Label Encoder',
    },
    'ORDINAL_ENCODER': {
        'class': OrdinalEncoder(),
        'label': 'OrdinalEncoder',
    },
}