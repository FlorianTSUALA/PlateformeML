""" Utility functions used by the tool """
from hashlib import md5
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pathlib
import json


def file_extention(path):
    return pathlib.Path(path).suffix

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def _delete_file(path):
   """ Deletes file from filesystem. """
   if os.path.isfile(path):
       os.remove(path)


def hash_file(path):
    """ Returns md5 hash of a file"""
    chk = md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            chk.update(chunk)
    return chk.hexdigest()
