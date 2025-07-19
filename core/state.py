CURRENT_MODULE = None


def get_current_module():
    return CURRENT_MODULE


def set_current_module(mod):
    global CURRENT_MODULE
    CURRENT_MODULE = mod
