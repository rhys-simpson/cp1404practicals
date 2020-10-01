"""
CP1404 practical
Kivy GUI pass/fail calculator
Rhys Simpson
"""

from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder


class GradeCalculatorApp(App):
    """Program calculating score/grade"""

    def build(self):
        """Build the Kivy app from the kv file"""
        Window.size = (600, 300)
        self.title = "Grade Calculator"
        self.root = Builder.load_file("scores.kv")
        return self.root

    def handle_calculate(self):
        """Handle score calculation"""
        self.root.ids.output_label.text = self.get_score()

    def handle_clear(self):
        """Handle clearing input box"""
        self.root.ids.output_label.text = "Enter your score out of 100"
        self.root.ids.input_score.text = ""

    def get_score(self):
        score = int(self.root.ids.input_score.text)
        if score < 0 or score > 100:
            return "Invalid Score"
        elif score >= 85:
            return "HD - High Distinction"
        elif score >= 75:
            return "D - Distinction"
        elif score >= 65:
            return "C - Credit"
        elif score >= 50:
            return "P - Pass"
        else:
            return "Fail"


GradeCalculatorApp().run()
