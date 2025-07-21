COMMAND_HANDLERS = {}


def register_command(name_or_dict, func=None):
    # Decorator usage: @register_command("foo")
    if func is None and isinstance(name_or_dict, str):

        def decorator(f):
            COMMAND_HANDLERS[name_or_dict] = f
            return f

        return decorator

    # Dynamic usage: register_command("foo", foo_handler)
    elif isinstance(name_or_dict, str) and callable(func):
        COMMAND_HANDLERS[name_or_dict] = func
        return func

    # Bulk usage (optional): register_command({...})
    elif isinstance(name_or_dict, dict):
        for name, fn in name_or_dict.items():
            if not callable(fn):
                raise ValueError(f"Handler for '{name}' is not callable")
            COMMAND_HANDLERS[name] = fn
        return name_or_dict

    else:
        raise TypeError("Invalid arguments passed to register_command")
