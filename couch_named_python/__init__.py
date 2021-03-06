# Copyright 2011 (C) Daniel Richman; GNU GPL 3

# Utility functions for view functions

_current_vs = None
_current_funcs = None

def _set_vs(vs, funcs=[]):
    global _current_vs, _current_funcs
    _current_vs = vs
    _current_funcs = funcs

class VSFunc(object):
    """A callable object that proxies calls to the view server object"""

    def __init__(self, name):
        self.name = name

    def vs(self):
        global _current_vs, _current_funcs
        assert _current_vs
        assert self.name in _current_funcs
        return getattr(_current_vs, self.name)

    def __call__(self, *args, **kwargs):
        return self.vs()(*args, **kwargs)

for funcname in ["emit", "log", "start", "send", "get_row"]:
    locals()[funcname] = VSFunc(funcname)
del funcname

def version(version):
    """
    A function decorator that tags a function with its 'version'

    version should be an integer. It will be checked against the expected
    version stored in the design document when the function is loaded.
    """

    version = int(version)

    def decorate(func):
        func._cnp_version = version
        return func
    return decorate

def get_version(func):
    try:
        return func._cnp_version
    except AttributeError:
        return None

class ForbiddenError(Exception):
    pass

class UnauthorizedError(Exception):
    pass

class NotFoundError(Exception):
    pass

class Redirect(Exception):
    def __init__(self, url, permanent=False):
        self.url = url
        self.permanent = permanent

UnauthorisedError = UnauthorizedError # :-)
