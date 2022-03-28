

def class_builder(classname, superclasses=(), attributedict={}):
    NewClass = type(classname, superclasses, attributedict)
    return NewClass()