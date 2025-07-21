from core.base_plugin import Plugin


class Plugin(Plugin):
    def __init__(self):
        self.name = "history_plugin"

    def on_load(self, cli_context):
        print(f"[{self.name}] Plugin initialized.")

    def register_commands(self):
        def history_handler(args, shared_data):
            print("[*] Command history feature (placeholder)")

        return {"history2": history_handler}
