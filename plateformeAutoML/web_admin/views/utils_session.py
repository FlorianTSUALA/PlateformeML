""" Utility functions used by the tool """
from hashlib import md5
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pathlib
import json



def clean_session_project_creation(request):
    request.session.clear()
    #del request.session['key']

def clean_session(request):
    request.session.clear()
    # del request.session['key']