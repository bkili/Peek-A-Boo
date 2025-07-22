# /core/cli.py
import logging
import os

from core.commands import core, module_ops, config_ops, display, option_ops  # noqa
from core.completer import SmartCompleter
from core.registry import COMMAND_HANDLERS
from core.utils.formatter import printc
from core.config import get_global_config
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style

style = Style.from_dict({"prompt": "#00ff00 bold"})

settings = get_global_config()
history_settings = settings.get("HISTORY", {})

HISTORY_ENABLED = history_settings.get("HISTORY_ENABLED", True)
OBFUSCATE_VALUES_IN_HISTORY = history_settings.get("OBFUSCATE_VALUES_IN_HISTORY", False)
MAX_ENTRIES = history_settings.get("MAX_ENTRIES", 1000)
HISTORY_PATH = ".pb_history"


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

            write_history_entry(command, cmd, args)

            # Clear the command history if the command is 'clear history'
            if command == "clear" and args and args[0] == "history":
                with open(".pb_history", "w") as hist_file:
                    hist_file.write("")
                printc("Command history cleared.", level="success")
                continue

            if command == "use" and args and shared_data.get("CURRENT_MODULE"):
                cmd_module_name = args[0]
            completer.update_nested()
        else:
            printc(f"Unknown command: {command}", level="error")
            logging.warning(f"Unknown command: {command}")


# Write command to history
def write_history_entry(command, cmd, args):
    if HISTORY_ENABLED:
        # Ensure the file exists
        if not os.path.exists(HISTORY_PATH):
            with open(HISTORY_PATH, "w") as f:
                f.write("")

        # Obfuscate if needed
        if OBFUSCATE_VALUES_IN_HISTORY and command == "set" and args:
            obfuscated_args = [args[0]]
            if len(args) > 1:
                obfuscated_args += ["********"]
            hist_line = f"{command} {' '.join(obfuscated_args)}"
        else:
            hist_line = cmd.strip()

        # Read, append, trim, and write back
        with open(HISTORY_PATH, "r") as f:
            history_lines = f.readlines()

        history_lines.append(hist_line + "\n")

        if len(history_lines) > MAX_ENTRIES:
            history_lines = history_lines[-MAX_ENTRIES:]

        with open(HISTORY_PATH, "w") as f:
            f.writelines(history_lines)
