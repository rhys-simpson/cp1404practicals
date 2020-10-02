"""
CP1404 Practical - Kivy GUI program to convert temperatures (celsius and fahrenheit)
Rhys Simpson
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty
import keyboard


class ConvertCelsiusFahrenheitApp(App):
    """Kivy app for converting temperatures"""
    output_temp = StringProperty()

    def build(self):
        """ """
        Window.size = (600, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_temps.kv")
        return self.root

    def handle_calculate(self):
        """ """
        if self.root.ids.temp_label.text == 'Fahrenheit to Celsius':
            value = 5 / 9 * (self.validate_number() - 32)
        else:
            value = self.validate_number() * 9.0 / 5 + 32
        self.output_temp = str(value)

    def convert_celsius_fahrenheit(self):
        """ """
        self.root.ids.temp_label.text = 'Celsius to Fahrenheit'

    def convert_fahrenheit_celsius(self):
        """ """
        self.root.ids.temp_label.text = 'Fahrenheit to Celsius'

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


ConvertCelsiusFahrenheitApp().run()
