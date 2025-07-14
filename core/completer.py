from prompt_toolkit.completion import Completer, NestedCompleter, PathCompleter
from core.utils.listing import list_modules, list_plugins, list_exploits
from core.state import get_current_module
from prompt_toolkit.document import Document

class SmartCompleter(Completer):
    def __init__(self):
        self.path_completer = PathCompleter(expanduser=True, only_directories=False)
        self.update_nested()

    def update_nested(self):
        current = get_current_module()
        self.base_completer = NestedCompleter.from_nested_dict({
            "exit": None,
            "help": None,
            "use": {mod: None for mod in list_modules() + list_plugins() + list_exploits()},
            "info": {mod: None for mod in list_modules() + list_plugins() + list_exploits()},
            "list": {"modules": None, "plugins": None, "exploits": None},
            "search": None,
            "run": None,
            "reload": None,
            "save": {"config": None},
            "load": {"config": None, "module": None},
            "show": {"options": None, "summary": None},
            "set": {opt: None for opt in current.options} if current else {}
        })

    def get_completions(self, document, complete_event):
        words = document.text.strip().split()
        if len(words) >= 2 and words[0] == "load" and words[1] in {"config", "module"}:
            sub_path = document.text.partition(words[1])[2].strip()
            return self.path_completer.get_completions(Document(sub_path), complete_event)
        return self.base_completer.get_completions(document, complete_event)