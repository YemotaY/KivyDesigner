from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider

Builder.load_string('''
<Toolbox>:
    orientation: 'vertical'
    size_hint_x: 0.2
    Label:
        text: 'Toolbox'
    Button:
        text: 'Button'
        on_release: root.add_widget_to_area('Button')
    Button:
        text: 'Label'
        on_release: root.add_widget_to_area('Label')
    Button:
        text: 'Slider'
        on_release: root.add_widget_to_area('Slider')

<WidgetArea>:
    canvas.before:
        Color:
            rgba: 0.95, 0.95, 0.95, 1
        Rectangle:
            pos: self.pos
            size: self.size
''')

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

class Toolbox(BoxLayout):
    widget_area = ObjectProperty(None)

    def add_widget_to_area(self, widget_type):
        # Find the WidgetArea in the parent layout
        parent = self.parent
        if parent:
            for child in parent.children:
                if isinstance(child, WidgetArea):
                    child.add_widget_by_type(widget_type)
                    break

class DesignerRoot(BoxLayout):
    pass

class KivyDesignerApp(App):
    def build(self):
        root = DesignerRoot(orientation='horizontal')
        toolbox = Toolbox()
        widget_area = WidgetArea()
        root.add_widget(toolbox)
        root.add_widget(widget_area)
        return root

if __name__ == "__main__":
    KivyDesignerApp().run()
