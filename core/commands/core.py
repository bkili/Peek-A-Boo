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
