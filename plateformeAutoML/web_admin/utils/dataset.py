""" Utility functions used by the tool """
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pathlib
import json
from numpy import log as ln
import matplotlib.pyplot as plt

import io
import base64

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

 #to del    
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
    data = load_dataframe(path)
    return data[data.columns.intersection(cols)]

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def info_dataset(path):
    dataframe = load_dataframe(path)
    
    #begin empty_cols
    empty_cols = [col for col in dataframe.columns if dataframe[col].isnull().all()]
    dataframe.drop(empty_cols, axis=1, inplace=True)
    dropped_msg=""
    if empty_cols:
        dropped_msg = "Empty columns detected, dropped columns : "+str(empty_cols) 
    features = dataframe.columns
    #end empty_cols

    columns = dataframe.columns
    cols_info = {}
    TDD = fetch.get_taxonomie_type_donnee(True)
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
    # return cols_info, dataframe.to_json(orient="split")
    return cols_info, dataframe

def feateares_encoding(df, cols_info):
    """ Encodes data and returns new data """
    mask = df.dtypes==object
    #get_categorical()
    categorical = df.columns[mask].tolist()
    print(categorical)
    if categorical:
        print("crash")
        #Encoder foreach column
        le = LabelEncoder()
        df[categorical] = df[categorical].apply(lambda x: le.fit_transform(x.astype(str)))
        # df.to_csv(path, index=False)
    print("Not crash")
    return df

def hist_img(df, cols_info):
    images = {}
    df = feateares_encoding(df, cols_info)
    #to integrate
    empty_cols = [col for col in df.columns if df[col].isnull().all()]
    df.drop(empty_cols, axis=1, inplace=True)
    dropped_msg=""

    if empty_cols:
        dropped_msg = "Empty columns detected, dropped columns : %s "%str(empty_cols) 
    features = df.columns
    for i in range(len(features)):
        # plt.clf()
        s = io.BytesIO()
        df[features[i]].hist()
        # plt.savefig("static/images/figs/" + str(i), bbox_inches="tight", transparent=True)
        plt.savefig(s, format='png', bbox_inches="tight")
        plt.close()
        bs64_img = base64.b64encode(s.getvalue()).decode("utf-8").replace("\n", "")
        images[features[i]] = 'data:image/png;base64,%s' % bs64_img
        # images[features[i]] = '<img align="left" src="data:image/png;base64,%s">' % bs64_img
    return images
