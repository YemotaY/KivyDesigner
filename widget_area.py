from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.app import App
from kivy.lang import Builder

class WidgetArea(FloatLayout):
    def add_widget_by_type(self, widget_type):
        if widget_type == 'Button':
            w = Button(text='Button', size_hint=(None, None), size=(100, 50), pos=(100, 100))
        elif widget_type == 'Label':
            w = Label(text='Label', size_hint=(None, None), size=(100, 50), pos=(100, 200))
        elif widget_type == 'Slider':
            w = Slider(size_hint=(None, None), size=(150, 50), pos=(100, 300))
        else:
            return
        self.add_widget(w)

if __name__ == "__main__":
    Builder.load_string('''
<WidgetArea>:
    canvas.before:
        Color:
            rgba: 0.95, 0.95, 0.95, 1
        Rectangle:
            pos: self.pos
            size: self.size
''')
    class TestApp(App):
        def build(self):
            return WidgetArea()
    TestApp().run()
