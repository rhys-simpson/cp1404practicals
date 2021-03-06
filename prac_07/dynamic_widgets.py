"""
CP1404 Practical
Kivy GUI program with dynamic widgets
Rhys Simpson
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):
    """Program demoing dynamic widgets"""

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from list and add them to GUI"""
        names = ["Jim Bob", "Jeff Bob", "Jimmy Bob"]
        for name in names:
            label = Label(text=name)
            self.root.ids.entries_box.add_widget(label)


DynamicWidgetsApp().run()
