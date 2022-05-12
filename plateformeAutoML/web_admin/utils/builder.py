from io import BytesIO
import base64

def ploter_(df):
    plot = sns.countplot(data=df)
    plot_file = BytesIO() 
    plot.savefig(plot_file, format='png')
    encoded_file = base64.b64encode(plot_file.getValue())
    return encoded_filed

def class_builder(classname, superclasses=(), attributedict={}):
    NewClass = type(classname, superclasses, attributedict)
    return NewClass()