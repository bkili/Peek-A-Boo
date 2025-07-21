import os
import yaml
from core.utils.formatter import printc

DEFAULT_CONFIG_PATH = "config.yaml"

DEFAULT_CONFIG = {
    "ENABLED_PLUGINS": [],
}


def load_global_config(path: str = DEFAULT_CONFIG_PATH) -> dict:
    """Load the global configuration from a YAML file."""
    if not os.path.exists(path):
        with open(path, "w") as f:
            yaml.dump(DEFAULT_CONFIG, f, default_flow_style=False)
        printc(
            f"[!] Configuration file not found. Created default at {path}", level="info"
        )
    try:
        with open(path, "r") as file:
            config = yaml.safe_load(file)
            return config if isinstance(config, dict) else {}
    except yaml.YAMLError as e:
        printc(f"[!] Error parsing YAML config: {e}", level="error")
    return {}
