# core/state.py
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


def reload_global_config(config_path):
    """Force reload the config.yaml file and update the global config."""
    from core.config_ops import load_global_config

    new_config = load_global_config(config_path)
    set_global_config(new_config)
    return new_config
