# core/registry.py

COMMAND_HANDLERS = {}

def register_command(name):
    def decorator(func):
        COMMAND_HANDLERS[name] = func
        return func
    return decorator
