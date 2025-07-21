# core/config.py
import os
import yaml
from core.utils.formatter import printc

DEFAULT_CONFIG_PATH = "config.yaml"
DEFAULT_CONFIG = {
    "ENABLED_PLUGINS": [],
}

_cached_config = None  # Internal cache


def load_global_config(path: str = DEFAULT_CONFIG_PATH) -> dict:
    """Read YAML config from file."""
    if not os.path.exists(path):
        with open(path, "w") as f:
            yaml.dump(DEFAULT_CONFIG, f, default_flow_style=False)
        printc(f"[!] Configuration file not found. Created default at {path}", level="info")

    try:
        with open(path, "r") as file:
            raw = file.read()
            # print(f"[DEBUG] Raw config text:\n{raw}")
            config = yaml.safe_load(raw)
            # print(f"[DEBUG] Parsed config object: {config}")
            return config if isinstance(config, dict) else {}
    except yaml.YAMLError as e:
        printc(f"[!] Error parsing YAML config: {e}", level="error")
        return {}


def get_global_config(path: str = DEFAULT_CONFIG_PATH) -> dict:
    """Return cached config after first load."""
    global _cached_config
    if _cached_config is None:
        _cached_config = load_global_config(path)
    return _cached_config