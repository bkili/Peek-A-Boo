CURRENT_MODULE = None
_global_config = {}

def get_current_module():
    return CURRENT_MODULE

def set_current_module(mod):
    global CURRENT_MODULE
    CURRENT_MODULE = mod

def set_global_config(cfg: dict):
    global _global_config
    _global_config = cfg

def get_global_config():
    return _global_config