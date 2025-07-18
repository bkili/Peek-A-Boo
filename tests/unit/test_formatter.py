import unittest
from io import StringIO
import sys
from core.utils.formatter import printc
import os

class TestFormatterUtils(unittest.TestCase):
    def setUp(self):
        # Force enable colors for tests
        os.environ['FORCE_COLOR'] = '1'
        # Capture stdout
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        # Restore stdout
        sys.stdout = self.original_stdout
        # Clean up environment
        if 'FORCE_COLOR' in os.environ:
            del os.environ['FORCE_COLOR']

    def test_printc_info_level(self):
        printc("This is info", "info")
        output = self.held_output.getvalue()
        self.assertIn("\x1b[", output)

    def test_printc_error_level(self):
        printc("Something failed", "error")
        output = self.held_output.getvalue()
        self.assertIn("\x1b[", output)

    def test_printc_success_level(self):
        printc("Done!", "success")
        output = self.held_output.getvalue()
        self.assertIn("\x1b[", output)