# core/commands/option_ops.py
from core.registry import register_command
from core.state import get_current_module
from core.utils.formatter import printc


@register_command("set")
def handle_set(args, shared_data):
    mod = get_current_module()
    if not mod:
        printc("No module selected.", level="error")
        return
    if not args:
        printc("Usage: set <option> [value]", level="warn")
        return
    key = args[0]
    value = " ".join(args[1:]) if len(args) > 1 else ""
    mod.set_option(key, value)
    printc(f"[+] {key} set to {value}", level="success")
