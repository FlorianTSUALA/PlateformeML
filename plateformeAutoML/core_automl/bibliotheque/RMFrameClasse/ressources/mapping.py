"""


"""

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
        'class': StandardScaler(),
        'label':  'Standard Scaller',
        'parameter': ''
    },
}

MAPPING_IMPUTER = {
    'StandardScaler': {
        'class': StandardScaler(),
        'label':  'Standard Scaller',
    },
}

MAPPING_NORMALISATION = {
    'StandardScaler': {
        'class': StandardScaler(),
        'label':  'Standard Scaller',
    },
}

MAPPING_ENCODER = {
    "OneHotEncoder" : sklearn.preprocessing.OneHotEncoder,
    "OrdinalEncoder" : sklearn.preprocessing.OrdinalEncoder,
    "LabelEncoder" : sklearn.preprocessing.LabelEncoder,
}
