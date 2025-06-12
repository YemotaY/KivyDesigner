from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config

# Configure window
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'minimum_width', '800')
Config.set('graphics', 'minimum_height', '600')

from toolbox import Toolbox
from widget_area import WidgetArea
from property_editor import PropertyEditor

Builder.load_file('designer.kv')

class DesignerRoot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Kivy Designer - Visual GUI Builder"

class KivyDesignerApp(App):
    def build(self):
        self.title = "Kivy Designer - Visual GUI Builder"
        return DesignerRoot()

if __name__ == "__main__":
    KivyDesignerApp().run()
