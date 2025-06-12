from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.progressbar import ProgressBar
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.lang import Builder
from kivy.vector import Vector
import random

class DraggableWidget:
    """Mixin-Klasse für Drag-and-Drop-Funktionalität"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_touch_down=self.on_widget_touch_down)
        self.bind(on_touch_move=self.on_widget_touch_move)
        self.bind(on_touch_up=self.on_widget_touch_up)
        self.dragging = False
        self.drag_offset = (0, 0)

    def on_widget_touch_down(self, widget, touch):
        if self.collide_point(*touch.pos):
            self.dragging = True
            self.drag_offset = (touch.x - self.x, touch.y - self.y)
            # Widget auswählen
            if hasattr(self.parent, 'select_widget'):
                self.parent.select_widget(self)
            return True
        return False

    def on_widget_touch_move(self, widget, touch):
        if self.dragging and self.collide_point(*touch.pos):
            self.x = touch.x - self.drag_offset[0]
            self.y = touch.y - self.drag_offset[1]
            return True
        return False

    def on_widget_touch_up(self, widget, touch):
        if self.dragging:
            self.dragging = False
            return True
        return False

class DraggableButton(DraggableWidget, Button):
    pass

class DraggableLabel(DraggableWidget, Label):
    pass

class DraggableSlider(DraggableWidget, Slider):
    pass

class DraggableTextInput(DraggableWidget, TextInput):
    pass

class DraggableCheckBox(DraggableWidget, CheckBox):
    pass

class DraggableProgressBar(DraggableWidget, ProgressBar):
    pass

class WidgetArea(FloatLayout):
    property_editor = ObjectProperty(None)
    selected_widget = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.widgets_count = {'Button': 0, 'Label': 0, 'Slider': 0, 'TextInput': 0, 'CheckBox': 0, 'ProgressBar': 0}

    def add_widget_by_type(self, widget_type):
        """Fügt ein neues Widget zur Design-Area hinzu"""
        self.widgets_count[widget_type] += 1
        
        # Zufällige Position generieren
        x = random.randint(50, max(50, int(self.width - 150)))
        y = random.randint(50, max(50, int(self.height - 100)))
        
        if widget_type == 'Button':
            w = DraggableButton(
                text=f'Button {self.widgets_count[widget_type]}',
                size_hint=(None, None),
                size=(120, 50),
                pos=(x, y)
            )
        elif widget_type == 'Label':
            w = DraggableLabel(
                text=f'Label {self.widgets_count[widget_type]}',
                size_hint=(None, None),
                size=(100, 50),
                pos=(x, y)
            )
        elif widget_type == 'Slider':
            w = DraggableSlider(
                size_hint=(None, None),
                size=(150, 50),
                pos=(x, y),
                min=0,
                max=100,
                value=50
            )
        elif widget_type == 'TextInput':
            w = DraggableTextInput(
                text=f'TextInput {self.widgets_count[widget_type]}',
                size_hint=(None, None),
                size=(150, 40),
                pos=(x, y),
                multiline=False
            )
        elif widget_type == 'CheckBox':
            w = DraggableCheckBox(
                size_hint=(None, None),
                size=(50, 50),
                pos=(x, y)
            )
        elif widget_type == 'ProgressBar':
            w = DraggableProgressBar(
                size_hint=(None, None),
                size=(200, 30),
                pos=(x, y),
                max=100,
                value=50
            )
        else:
            return
        
        self.add_widget(w)
        self.select_widget(w)

    def select_widget(self, widget):
        """Wählt ein Widget aus und zeigt seine Eigenschaften"""
        # Entferne Auswahl von vorherigem Widget
        if self.selected_widget:
            if hasattr(self.selected_widget, 'canvas'):
                self.selected_widget.canvas.after.clear()
        
        self.selected_widget = widget
        
        # Füge visuelle Auswahl hinzu (roter Rahmen)
        if widget:
            with widget.canvas.after:
                from kivy.graphics import Color, Line
                Color(1, 0, 0, 1)  # Rot
                Line(rectangle=(widget.x, widget.y, widget.width, widget.height), width=2)
            
            # Aktualisiere Property Editor
            if self.property_editor:
                self.property_editor.update_properties(widget)

    def remove_selected_widget(self):
        """Entfernt das ausgewählte Widget"""
        if self.selected_widget:
            self.remove_widget(self.selected_widget)
            self.selected_widget = None
            if self.property_editor:
                self.property_editor.clear_properties()

    def on_touch_down(self, touch):
        # Prüfe zuerst, ob ein Widget getroffen wurde
        for child in reversed(self.children):
            if child.collide_point(*touch.pos):
                return child.dispatch('on_touch_down', touch)
        
        # Wenn kein Widget getroffen wurde, deselektiere
        self.select_widget(None)
        if self.property_editor:
            self.property_editor.clear_properties()
        return super().on_touch_down(touch)

if __name__ == "__main__":
    Builder.load_string('''
<WidgetArea>:
    canvas.before:
        Color:
            rgba: 0.98, 0.98, 0.98, 1
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: 0.8, 0.8, 0.8, 1
        Line:
            rectangle: self.x, self.y, self.width, self.height
''')
    class TestApp(App):
        def build(self):
            return WidgetArea()
    TestApp().run()
