"""
CP1404 practical
Kivy GUI buttons demo
Rhys Simpson
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Program demoing buttons"""

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle output label text"""
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def handle_clear(self):
        """Handle clearing input box"""
        self.root.ids.output_label.text = "Enter your name"
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
