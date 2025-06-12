from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.clock import Clock

class PropertyEditor(BoxLayout):
    selected_widget = ObjectProperty(None, allownone=True)
    widget_area = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.property_inputs = {}

    def update_properties(self, widget):
        """Aktualisiert den Eigenschaften-Editor für das ausgewählte Widget"""
        self.selected_widget = widget
        self.clear_properties()
        
        if not widget:
            return
        
        container = self.ids.properties_container
        
        # Widget-Typ anzeigen
        type_label = Label(
            text=f'Widget: {widget.__class__.__name__}',
            size_hint_y=None,
            height=30,
            bold=True
        )
        container.add_widget(type_label)
        
        # Position Eigenschaften
        self.add_property_section(container, "Position & Größe")
        self.add_position_properties(container, widget)
        
        # Text Eigenschaften (wenn applicable)
        if hasattr(widget, 'text'):
            self.add_property_section(container, "Text")
            self.add_text_properties(container, widget)
        
        # Spezielle Eigenschaften
        if widget.__class__.__name__ == 'Slider':
            self.add_property_section(container, "Slider")
            self.add_slider_properties(container, widget)
        elif widget.__class__.__name__ == 'ProgressBar':
            self.add_property_section(container, "Progress Bar")
            self.add_progressbar_properties(container, widget)
        elif widget.__class__.__name__ == 'CheckBox':
            self.add_property_section(container, "CheckBox")
            self.add_checkbox_properties(container, widget)
        
        # Delete Button
        self.add_property_section(container, "Aktionen")
        delete_btn = Button(
            text='Widget löschen',
            size_hint_y=None,
            height=40,
            background_color=(1, 0.3, 0.3, 1)
        )
        delete_btn.bind(on_release=lambda x: self.delete_widget())
        container.add_widget(delete_btn)

    def add_property_section(self, container, title):
        """Fügt eine Sektions-Überschrift hinzu"""
        section_label = Label(
            text=title,
            size_hint_y=None,
            height=25,
            bold=True,
            color=(0.2, 0.2, 0.8, 1)
        )
        container.add_widget(section_label)

    def add_position_properties(self, container, widget):
        """Fügt Position und Größen-Eigenschaften hinzu"""
        # X Position
        x_layout = BoxLayout(size_hint_y=None, height=30)
        x_layout.add_widget(Label(text='X:', size_hint_x=0.3))
        x_input = TextInput(
            text=str(int(widget.x)),
            multiline=False,
            size_hint_x=0.7
        )
        x_input.bind(text=lambda instance, value: self.update_widget_property('x', value))
        x_layout.add_widget(x_input)
        container.add_widget(x_layout)
        self.property_inputs['x'] = x_input
        
        # Y Position
        y_layout = BoxLayout(size_hint_y=None, height=30)
        y_layout.add_widget(Label(text='Y:', size_hint_x=0.3))
        y_input = TextInput(
            text=str(int(widget.y)),
            multiline=False,
            size_hint_x=0.7
        )
        y_input.bind(text=lambda instance, value: self.update_widget_property('y', value))
        y_layout.add_widget(y_input)
        container.add_widget(y_layout)
        self.property_inputs['y'] = y_input
        
        # Width
        w_layout = BoxLayout(size_hint_y=None, height=30)
        w_layout.add_widget(Label(text='Breite:', size_hint_x=0.3))
        w_input = TextInput(
            text=str(int(widget.width)),
            multiline=False,
            size_hint_x=0.7
        )
        w_input.bind(text=lambda instance, value: self.update_widget_property('width', value))
        w_layout.add_widget(w_input)
        container.add_widget(w_layout)
        self.property_inputs['width'] = w_input
        
        # Height
        h_layout = BoxLayout(size_hint_y=None, height=30)
        h_layout.add_widget(Label(text='Höhe:', size_hint_x=0.3))
        h_input = TextInput(
            text=str(int(widget.height)),
            multiline=False,
            size_hint_x=0.7
        )
        h_input.bind(text=lambda instance, value: self.update_widget_property('height', value))
        h_layout.add_widget(h_input)
        container.add_widget(h_layout)
        self.property_inputs['height'] = h_input

    def add_text_properties(self, container, widget):
        """Fügt Text-Eigenschaften hinzu"""
        text_layout = BoxLayout(size_hint_y=None, height=30)
        text_layout.add_widget(Label(text='Text:', size_hint_x=0.3))
        text_input = TextInput(
            text=widget.text,
            multiline=False,
            size_hint_x=0.7
        )
        text_input.bind(text=lambda instance, value: self.update_widget_property('text', value))
        text_layout.add_widget(text_input)
        container.add_widget(text_layout)
        self.property_inputs['text'] = text_input

    def add_slider_properties(self, container, widget):
        """Fügt Slider-spezifische Eigenschaften hinzu"""
        # Min Value
        min_layout = BoxLayout(size_hint_y=None, height=30)
        min_layout.add_widget(Label(text='Min:', size_hint_x=0.3))
        min_input = TextInput(
            text=str(widget.min),
            multiline=False,
            size_hint_x=0.7
        )
        min_input.bind(text=lambda instance, value: self.update_widget_property('min', value))
        min_layout.add_widget(min_input)
        container.add_widget(min_layout)
        self.property_inputs['min'] = min_input
        
        # Max Value
        max_layout = BoxLayout(size_hint_y=None, height=30)
        max_layout.add_widget(Label(text='Max:', size_hint_x=0.3))
        max_input = TextInput(
            text=str(widget.max),
            multiline=False,
            size_hint_x=0.7
        )
        max_input.bind(text=lambda instance, value: self.update_widget_property('max', value))
        max_layout.add_widget(max_input)
        container.add_widget(max_layout)
        self.property_inputs['max'] = max_input
        
        # Current Value
        value_layout = BoxLayout(size_hint_y=None, height=30)
        value_layout.add_widget(Label(text='Wert:', size_hint_x=0.3))
        value_input = TextInput(
            text=str(widget.value),
            multiline=False,
            size_hint_x=0.7
        )
        value_input.bind(text=lambda instance, value: self.update_widget_property('value', value))
        value_layout.add_widget(value_input)
        container.add_widget(value_layout)
        self.property_inputs['value'] = value_input

    def add_progressbar_properties(self, container, widget):
        """Fügt ProgressBar-spezifische Eigenschaften hinzu"""
        # Max Value
        max_layout = BoxLayout(size_hint_y=None, height=30)
        max_layout.add_widget(Label(text='Max:', size_hint_x=0.3))
        max_input = TextInput(
            text=str(widget.max),
            multiline=False,
            size_hint_x=0.7
        )
        max_input.bind(text=lambda instance, value: self.update_widget_property('max', value))
        max_layout.add_widget(max_input)
        container.add_widget(max_layout)
        self.property_inputs['max'] = max_input
        
        # Current Value
        value_layout = BoxLayout(size_hint_y=None, height=30)
        value_layout.add_widget(Label(text='Wert:', size_hint_x=0.3))
        value_input = TextInput(
            text=str(widget.value),
            multiline=False,
            size_hint_x=0.7
        )
        value_input.bind(text=lambda instance, value: self.update_widget_property('value', value))
        value_layout.add_widget(value_input)
        container.add_widget(value_layout)
        self.property_inputs['value'] = value_input

    def add_checkbox_properties(self, container, widget):
        """Fügt CheckBox-spezifische Eigenschaften hinzu"""
        active_layout = BoxLayout(size_hint_y=None, height=30)
        active_layout.add_widget(Label(text='Aktiv:', size_hint_x=0.3))
        active_checkbox = CheckBox(
            active=widget.active,
            size_hint_x=0.7
        )
        active_checkbox.bind(active=lambda instance, value: self.update_widget_property('active', value))
        active_layout.add_widget(active_checkbox)
        container.add_widget(active_layout)
        self.property_inputs['active'] = active_checkbox

    def update_widget_property(self, property_name, value):
        """Aktualisiert eine Eigenschaft des ausgewählten Widgets"""
        if not self.selected_widget:
            return
        
        try:
            if property_name in ['x', 'y', 'width', 'height']:
                setattr(self.selected_widget, property_name, float(value))
                # Widget-Auswahl aktualisieren
                if self.widget_area:
                    Clock.schedule_once(lambda dt: self.widget_area.select_widget(self.selected_widget), 0.1)
            elif property_name in ['min', 'max', 'value']:
                setattr(self.selected_widget, property_name, float(value))
            elif property_name == 'text':
                setattr(self.selected_widget, property_name, str(value))
            elif property_name == 'active':
                setattr(self.selected_widget, property_name, bool(value))
        except (ValueError, TypeError):
            pass  # Ignore invalid values

    def clear_properties(self):
        """Leert den Eigenschaften-Editor"""
        if hasattr(self, 'ids') and 'properties_container' in self.ids:
            self.ids.properties_container.clear_widgets()
        self.property_inputs.clear()

    def delete_widget(self):
        """Löscht das ausgewählte Widget"""
        if self.widget_area and self.selected_widget:
            self.widget_area.remove_selected_widget()

if __name__ == "__main__":
    from kivy.app import App
    from kivy.lang import Builder
    Builder.load_string('''
<PropertyEditor>:
    orientation: 'vertical'
    Label:
        text: 'Eigenschaften'
        size_hint_y: None
        height: 30
        bold: True
    ScrollView:
        GridLayout:
            id: properties_container
            cols: 1
            spacing: 5
            size_hint_y: None
            height: self.minimum_height
''')
    class TestApp(App):
        def build(self):
            return PropertyEditor()
    TestApp().run()
