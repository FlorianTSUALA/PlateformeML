""" Utility functions used by the tool """
from hashlib import md5
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pathlib

def file_extention(path):
    return pathlib.Path(path).suffix

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_dataframe(path):
    print((path))
    if file_extention(path) == '.csv':
        return pd.read_csv(path,sep=sep)
    elif file_extention(path) == '.xls' or  file_extention(path) == '.xlsx'  :
        return pd.read_excel(path)
    else:
        return
     
#################################################################   DATA EXPLORATION

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

def info_dataset(path):
    dataframe = load_dataframe(path)
    columns = dataframe.columns
    col_sheet_name = {}
    for col in columns:
        macolonne = {}
        macolonne["type"] = dataframe[col].dtype
        macolonne["data"] = list(dataframe[col])

        if (dataframe[col].dtype == "int64" or dataframe[col].dtype == "int32"):
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
        col_sheet_name[col] = macolonne

    return col_sheet_name

def _delete_file(path):
   """ Deletes file from filesystem. """
   if os.path.isfile(path):
       os.remove(path)

############################################################    SESSION

def clean_session_project_creation(request):
    request.session.clear()
    #del request.session['key']

def clean_session(request):
    request.session.clear()
    # del request.session['key']

def hash_file(path):
    """ Returns md5 hash of a file"""
    chk = md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            chk.update(chunk)
    return chk.hexdigest()
