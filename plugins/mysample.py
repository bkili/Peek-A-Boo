# mypsample.py
import logging

from modules.base import BaseModule

class Module(BaseModule):
    def __init__(self):
        super().__init__()
        self.name = "mysample"
        self.description = "A simple test plugin loaded from external path."
        self.author = "sample"
        self.author_email = "sample@proton.me"
        self.url = "sample.com"
        self.license = "SampleLicense"
        self.version = "0.0.1"
        self.default_options = {
            "example_option": "default_value"
        }
        self.required_options = ["example_option"]
        self.options = self.default_options.copy()

    def run(self, shared_data):
        print(f"[{self.name}] Running test plugin with option: {self.options['example_option']}")
        shared_data["last_summary"] = {
            "module": self.name,
            "option_used": self.options["example_option"]
        }

    def print_summary(self, summary):
        try:
            print(f"Option used : {summary.get('option_used', '-')}")
        except:
            logging.error(f"Error")