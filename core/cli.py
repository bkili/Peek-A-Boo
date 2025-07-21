# /core/cli.py
import logging

from core.commands import core, module_ops, config_ops, display, option_ops  # noqa
from core.completer import SmartCompleter
from core.registry import COMMAND_HANDLERS
from core.utils.formatter import printc
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style

style = Style.from_dict({"prompt": "#00ff00 bold"})


def start_cli():
    shared_data = {}
    cmd_module_name = ""
    completer = SmartCompleter()
    session = PromptSession(
        message=lambda: f"[{cmd_module_name}]> ", completer=completer, style=style
    )
    printc(
        "Welcome to Peek-A-Boo CLI. Type 'help' to see available commands.",
        level="headline",
    )

    while True:
        try:
            cmd = session.prompt()
        except (EOFError, KeyboardInterrupt):
            printc("Exiting...", level="warn")
            break

        if not cmd.strip():
            continue

        parts = cmd.strip().split()
        command = parts[0]
        args = parts[1:]

        handler = COMMAND_HANDLERS.get(command)
        if handler:
            handler(args, shared_data)
            with open(".pb_history", "a") as hist_file:
                hist_file.write(cmd.strip() + "\n")
            if command == "use" and args and shared_data.get("CURRENT_MODULE"):
                cmd_module_name = args[0]
            completer.update_nested()
        else:
            printc(f"Unknown command: {command}", level="error")
            logging.warning(f"Unknown command: {command}")
