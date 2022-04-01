from io import BytesIO
import base64

def booking_hour_plot():
    qs = bookings_today()
    df = read_frame(qs)
    plot = sns.countplot(data=df)
    plot_file = BytesIO() 
    plot.savefig(plot_file, format='png')
    encoded_file - base64.b64encode(plot_file.getValue())
    return encoded_filed

def class_builder(classname, superclasses=(), attributedict={}):
    NewClass = type(classname, superclasses, attributedict)
    return NewClass()