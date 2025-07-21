# core/base_plugin.py


class Plugin:
    def __init__(self):
        self.name = "base"

    def on_load(self, cli_context):
        """Called when plugin is loaded. Optional."""
        pass

    def register_commands(self):
        """Return a dict of custom commands."""
        return {}
