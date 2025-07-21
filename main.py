from core.config import get_global_config as load_config
from core.plugin import load_plugins
from core.cli import start_cli
from core.registry import register_command
from core.state import set_global_config, get_global_config

# Load and store global configuration
config = load_config()
set_global_config(config)

# Access plugin list from stored config
ENABLED_PLUGINS = get_global_config().get("ENABLED_PLUGINS", [])

# CLI context vars like shared_data or command registry
cli_context = {}

# Load plugins before CLI starts
loaded_plugins = load_plugins(ENABLED_PLUGINS, cli_context)

# Register plugin CLI commands
for plugin in loaded_plugins.values():
    try:
        commands = plugin.register_commands()
        if isinstance(commands, dict):
            register_command(commands)
    except Exception as e:
        print(f"[!] Failed to register plugin commands for {plugin.name}: {e}")

if __name__ == "__main__":
    start_cli()
