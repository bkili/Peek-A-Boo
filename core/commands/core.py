# core/commands/core.py
from core.registry import register_command
from core.utils.formatter import printc
import sys
import os


@register_command("exit")
def handle_exit(args, shared_data):
    printc("Exiting...", level="warn")
    sys.exit()


@register_command("help")
def handle_help(args, shared_data):
    from core.registry import COMMAND_HANDLERS

    printc("Available commands:", level="info")
    for cmd in sorted(COMMAND_HANDLERS):
        print(f"  - {cmd}")


@register_command("clear")
def handle_clear(args, shared_data):
    os.system("cls" if os.name == "nt" else "clear")


@register_command("history")
def handle_history(args, shared_data):
    path = ".pb_history"
    if not os.path.exists(path):
        printc("No command history found.", level="warn")
        return
    
    try:
        with open(path, "r") as file:
            history = file.read().strip()
            if history:
                printc("Command History:", level="selection")
                for line in history.splitlines():
                    printc(f"{line}", level="info")
            else:
                printc("No command history found.", level="warn")
    except Exception as e:
        printc(f"[!] Failed to read history: {e}", level="error")


@register_command("debug")
def handle_debug(args, shared_data):
    for arg in args:
        print(f"Debug argument: {arg}")
