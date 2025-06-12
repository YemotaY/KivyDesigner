# Demo-Layout für den Kivy Designer
# Diese Datei kann als Vorlage oder Test verwendet werden

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider

class DemoLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Demo Button
        demo_button = Button(
            text='Demo Button',
            pos=(50, 300),
            size=(120, 50),
            size_hint=(None, None)
        )
        self.add_widget(demo_button)
        
        # Demo Label
        demo_label = Label(
            text='Demo Label',
            pos=(200, 300),
            size=(100, 50),
            size_hint=(None, None)
        )
        self.add_widget(demo_label)
        
        # Demo Slider
        demo_slider = Slider(
            pos=(50, 200),
            size=(200, 50),
            size_hint=(None, None),
            min=0,
            max=100,
            value=50
        )
        self.add_widget(demo_slider)

class DemoApp(App):
    def build(self):
        self.title = "Kivy Designer - Demo Layout"
        return DemoLayout()

if __name__ == "__main__":
    DemoApp().run()
