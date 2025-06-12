from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
import os
from exporter import export_to_kv, export_to_py

class Toolbox(BoxLayout):
    widget_area = ObjectProperty(None)
    property_editor = ObjectProperty(None)

    def add_widget_to_area(self, widget_type):
        """Fügt ein Widget zur WidgetArea hinzu"""
        if self.widget_area:
            self.widget_area.add_widget_by_type(widget_type)

    def export_kv(self):
        """Exportiert das aktuelle Layout als .kv Datei"""
        content = BoxLayout(orientation='vertical')
        filechooser = FileChooserIconView(
            path=os.getcwd(),
            filters=['*.kv']
        )
        content.add_widget(filechooser)
        
        button_layout = BoxLayout(size_hint_y=None, height=50)
        save_btn = Button(text='Speichern')
        cancel_btn = Button(text='Abbrechen')
        button_layout.add_widget(save_btn)
        button_layout.add_widget(cancel_btn)
        content.add_widget(button_layout)
        
        popup = Popup(title='Als .kv Datei speichern', content=content, size_hint=(0.8, 0.8))
        
        def save_file(instance):
            if filechooser.selection:
                filepath = filechooser.selection[0]
                if not filepath.endswith('.kv'):
                    filepath += '.kv'
            else:
                filepath = os.path.join(filechooser.path, 'layout.kv')
            
            try:
                export_to_kv(self.widget_area, filepath)
                popup.dismiss()
            except Exception as e:
                print(f"Fehler beim Exportieren: {e}")
        
        save_btn.bind(on_release=save_file)
        cancel_btn.bind(on_release=popup.dismiss)
        popup.open()

    def export_py(self):
        """Exportiert das aktuelle Layout als Python Datei"""
        content = BoxLayout(orientation='vertical')
        filechooser = FileChooserIconView(
            path=os.getcwd(),
            filters=['*.py']
        )
        content.add_widget(filechooser)
        
        button_layout = BoxLayout(size_hint_y=None, height=50)
        save_btn = Button(text='Speichern')
        cancel_btn = Button(text='Abbrechen')
        button_layout.add_widget(save_btn)
        button_layout.add_widget(cancel_btn)
        content.add_widget(button_layout)
        
        popup = Popup(title='Als Python Datei speichern', content=content, size_hint=(0.8, 0.8))
        
        def save_file(instance):
            if filechooser.selection:
                filepath = filechooser.selection[0]
                if not filepath.endswith('.py'):
                    filepath += '.py'
            else:
                filepath = os.path.join(filechooser.path, 'layout.py')
            
            try:
                export_to_py(self.widget_area, filepath)
                popup.dismiss()
            except Exception as e:
                print(f"Fehler beim Exportieren: {e}")
        
        save_btn.bind(on_release=save_file)
        cancel_btn.bind(on_release=popup.dismiss)
        popup.open()

# Entferne doppelte Definitionen - diese sind jetzt in widget_area.py
