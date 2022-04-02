""" Utility functions used by the tool """
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pathlib
import json

from webapp.utils.file import file_extention

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
    col_sheet_name = {}
    for col in columns:
        macolonne = {}
        macolonne["type"] = str(dataframe[col].dtype)
        # macolonne["data"] = dataframe[col].to_json()
        macolonne["data"] = json.dumps(dataframe[col].values.tolist())

        if (dataframe[col].dtype == np.int64 or dataframe[col].dtype == np.int32):
            macolonne["scaler"] = "Standard_Scaler"
            macolonne["imputer"] = "Mean"
            macolonne["encoder"] = "None"
            if dataframe[col].count() < 10:
                macolonne["nature"] = "discret"
            else:
                macolonne["nature"] = "continue"

        elif (dataframe[col].dtype == "bool"):
            macolonne["scaler"] = "None"
            macolonne["imputer"] = "Most_frequent"
            macolonne["encoder"] = "OneHot_Encoder"

            macolonne["nature"] = "discret"
        else:
            macolonne["scaler"] = "None"
            macolonne["imputer"] = "Most_frequent"
            macolonne["encoder"] = "OneHot_Encoder"

            macolonne["nature"] = "categoriel"
        col_sheet_name[(col)] = macolonne
    print(col_sheet_name)
    # return json.dumps(col_sheet_name, cls=NumpyEncoder)
    return (col_sheet_name, dataframe.to_json())