""" Utility functions used by the tool """

def clean_session_projet_creation(request):
    request.session.clear()
    #del request.session['key']

def clean_session(request):
    request.session.clear()
    # del request.session['key']