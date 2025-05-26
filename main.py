from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from toolbox import Toolbox
from widget_area import WidgetArea
from property_editor import PropertyEditor

Builder.load_file('designer.kv')

class DesignerRoot(BoxLayout):
    pass

class KivyDesignerApp(App):
    def build(self):
        return DesignerRoot()

if __name__ == "__main__":
    KivyDesignerApp().run()
