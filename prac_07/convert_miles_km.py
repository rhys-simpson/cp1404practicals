"""
CP1404 Practical
Kivy GUI program to convert miles to km
Rhys Simpson
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

MILES_TO_KM_NUMBER = 1.60934


class ConvertMilesToKMApp(App):
    """Kivy app for converting miles to km"""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (500, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculate(self):
        """Handle calculation of miles to km"""
        value = self.validate_number() * MILES_TO_KM_NUMBER
        self.output_km = str(value)

    def handle_increment(self, change):
        """Handle up/down button press, update input box"""
        value = self.validate_number() + change
        self.root.ids.input_number.text = str(value)

    def validate_number(self):
        """Validate user input number"""
        try:
            return float(self.root.ids.input_number.text)
        except ValueError:
            return 0.0


ConvertMilesToKMApp().run()
