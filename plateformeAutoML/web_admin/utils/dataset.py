""" Utility functions used by the tool """
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pathlib
import json
from numpy import log as ln

from .file import file_extention
from web_admin.services import fetch_config as fetch


def load_dataframe(path,sep=','):
    extention = file_extention(path)
    if extention == '.csv':
        return pd.read_csv(path,sep=sep)
    elif extention == '.xls' or  extention == '.xlsx'  :
        return pd.read_excel(path)
    elif extention == '.npy':
        np.load(path)
    else:
        return []
     
def load_initial(path,sep=','):
    """ Encodes data and returns new data """
    data = load_dataframe(path)
    mask = data.dtypes==object
    categorical = data.columns[mask].tolist()
    print(categorical)
    if categorical:
        print("crash")
        le = LabelEncoder()
        data[categorical] = data[categorical].apply(lambda x: le.fit_transform(x.astype(str)))
        data.to_csv(path, index=False)
    print("Not crash")
    return data

def return_cols(path):
    """ Returns column names of the CSV"""
    data = load_dataframe(path)
    return list(data.columns)

def select_cols(path, cols):
    """Select passed columns from the CSV"""
    data = pd.read_csv(path)
    return data[data.columns.intersection(cols)]

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def info_dataset(path):
    dataframe = load_dataframe(path)
    columns = dataframe.columns
    cols_info = {}
    TDD = fetch.get_taxonomie_type_donnee(True)
    # print(TDD)
    TDD_TYPE_KEY = dict((values['type'],key) for key, values in TDD.items())
    for col_name in columns:
        col_info = {}
        col_info['type'] = TDD_TYPE_KEY[str(dataframe[col_name].dtype)]
        # col_info["data"] = dataframe[col].to_json()
        # col_info["data"] = json.dumps(dataframe[col_name].values.tolist())
        col_info['nature'] = 'CATEGORIEL'
        if dataframe[col_name].dtype in [ *TDD['ENTIER']['data'], *TDD['ENTIER']['data'], *TDD['DATE']['data'], *TDD['TIMEDELTA']['data'] ]:
            if len(dataframe[col_name].unique())  > ln(len(dataframe))**2/3:
                col_info['nature'] = 'QUATITATIF'
        
        #TODO Make more controll
        #TODO Check to DB
        col_info['scaller'] = TDD[col_info['type']]['preprocessing']['scaller']
        col_info['imputer'] = TDD[col_info['type']]['preprocessing']['imputer']
        col_info['encoder'] = TDD[col_info['type']]['preprocessing']['encoder']

        cols_info[col_name] = col_info
    # return json.dumps(cols_info, cls=NumpyEncoder)
    return cols_info, dataframe