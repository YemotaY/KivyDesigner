# Generiert von Kivy Designer am 2025-06-12 11:13:12

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.slider import Slider

class GeneratedLayout(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        slider_1 = Slider(
            pos=(50, 200),
            size=(100, 50),
            size_hint=(None, None),
            text="Test Button"
        )
        self.add_widget(slider_1)
        
        slider_2 = Slider(
            pos=(200, 200),
            size=(100, 50),
            size_hint=(None, None),
            text="Test Label"
        )
        self.add_widget(slider_2)
        
        slider_3 = Slider(
            pos=(50, 100),
            size=(150, 50),
            size_hint=(None, None),
            min=0,
            max=100,
            value=50
        )
        self.add_widget(slider_3)
        

if __name__ == "__main__":
    from kivy.app import App

    class GeneratedApp(App):
        def build(self):
            return GeneratedLayout()

    GeneratedApp().run()