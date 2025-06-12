import os
from datetime import datetime

def export_to_kv(widget_area, filename):
    """Exportiert das Widget-Layout als .kv Datei"""
    if not widget_area or not widget_area.children:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('# Leeres Layout - keine Widgets vorhanden\n')
            f.write('<FloatLayout>:\n')
            f.write('    pass\n')
        return
    
    kv_content = []
    kv_content.append(f'# Generiert von Kivy Designer am {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    kv_content.append('')
    kv_content.append('<GeneratedLayout>:')
    
    # Widgets durchgehen und KV-Code generieren
    for widget in widget_area.children:
        widget_kv = generate_kv_for_widget(widget)
        if widget_kv:
            for line in widget_kv:
                kv_content.append(f'    {line}')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(kv_content))
    
    print(f"Layout als .kv Datei exportiert: {filename}")

def export_to_py(widget_area, filename):
    """Exportiert das Widget-Layout als Python Datei"""
    if not widget_area or not widget_area.children:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('# Leeres Layout - keine Widgets vorhanden\n')
            f.write('from kivy.uix.floatlayout import FloatLayout\n\n')
            f.write('class GeneratedLayout(FloatLayout):\n')
            f.write('    pass\n')
        return
    
    py_content = []
    py_content.append(f'# Generiert von Kivy Designer am {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    py_content.append('')
    
    # Imports sammeln
    imports = set(['from kivy.uix.floatlayout import FloatLayout'])
    for widget in widget_area.children:
        widget_import = get_import_for_widget(widget)
        if widget_import:
            imports.add(widget_import)
    
    # Imports schreiben
    for imp in sorted(imports):
        py_content.append(imp)
    
    py_content.append('')
    py_content.append('class GeneratedLayout(FloatLayout):')
    py_content.append('    def __init__(self, **kwargs):')
    py_content.append('        super().__init__(**kwargs)')
    py_content.append('')
    
    # Widgets hinzufügen
    widget_counter = {}
    for widget in widget_area.children:
        widget_code = generate_python_for_widget(widget, widget_counter)
        if widget_code:
            for line in widget_code:
                py_content.append(f'        {line}')
    
    py_content.append('')
    py_content.append('if __name__ == "__main__":')
    py_content.append('    from kivy.app import App')
    py_content.append('')
    py_content.append('    class GeneratedApp(App):')
    py_content.append('        def build(self):')
    py_content.append('            return GeneratedLayout()')
    py_content.append('')
    py_content.append('    GeneratedApp().run()')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(py_content))
    
    print(f"Layout als Python Datei exportiert: {filename}")

def generate_kv_for_widget(widget):
    """Generiert KV-Code für ein einzelnes Widget"""
    widget_type = widget.__class__.__name__
    if widget_type.startswith('Draggable'):
        widget_type = widget_type[9:]  # Entferne 'Draggable' Prefix
    
    kv_lines = []
    kv_lines.append(f'{widget_type}:')
    
    # Position und Größe
    kv_lines.append(f'    pos: {int(widget.x)}, {int(widget.y)}')
    kv_lines.append(f'    size: {int(widget.width)}, {int(widget.height)}')
    kv_lines.append('    size_hint: None, None')
      # Widget-spezifische Eigenschaften
    if hasattr(widget, 'text') and widget.text:
        kv_lines.append(f'    text: "{widget.text}"')
    
    if widget_type == 'Slider':
        if hasattr(widget, 'min'):
            kv_lines.append(f'    min: {widget.min}')
        if hasattr(widget, 'max'):
            kv_lines.append(f'    max: {widget.max}')
        if hasattr(widget, 'value'):
            kv_lines.append(f'    value: {widget.value}')
    elif widget_type == 'ProgressBar':
        if hasattr(widget, 'max'):
            kv_lines.append(f'    max: {widget.max}')
        if hasattr(widget, 'value'):
            kv_lines.append(f'    value: {widget.value}')
    elif widget_type == 'CheckBox':
        if hasattr(widget, 'active'):
            kv_lines.append(f'    active: {str(widget.active).lower()}')
    
    return kv_lines

def generate_python_for_widget(widget, widget_counter):
    """Generiert Python-Code für ein einzelnes Widget"""
    widget_type = widget.__class__.__name__
    if widget_type.startswith('Draggable'):
        widget_type = widget_type[9:]  # Entferne 'Draggable' Prefix
    
    # Widget-Counter für eindeutige Namen
    if widget_type not in widget_counter:
        widget_counter[widget_type] = 0
    widget_counter[widget_type] += 1
    widget_name = f'{widget_type.lower()}_{widget_counter[widget_type]}'
    
    py_lines = []
    
    # Widget erstellen
    widget_args = []
    widget_args.append(f'pos=({int(widget.x)}, {int(widget.y)})')
    widget_args.append(f'size=({int(widget.width)}, {int(widget.height)})')
    widget_args.append('size_hint=(None, None)')
    
    # Widget-spezifische Eigenschaften
    if hasattr(widget, 'text') and widget.text:
        widget_args.append(f'text="{widget.text}"')
    if widget_type == 'Slider':
        if hasattr(widget, 'min'):
            widget_args.append(f'min={widget.min}')
        if hasattr(widget, 'max'):
            widget_args.append(f'max={widget.max}')
        if hasattr(widget, 'value'):
            widget_args.append(f'value={widget.value}')
    elif widget_type == 'ProgressBar':
        if hasattr(widget, 'max'):
            widget_args.append(f'max={widget.max}')
        if hasattr(widget, 'value'):
            widget_args.append(f'value={widget.value}')
    elif widget_type == 'CheckBox':
        if hasattr(widget, 'active'):
            widget_args.append(f'active={widget.active}')
    
    # Widget erstellen und hinzufügen
    py_lines.append(f'{widget_name} = {widget_type}(')
    for i, arg in enumerate(widget_args):
        suffix = ',' if i < len(widget_args) - 1 else ''
        py_lines.append(f'    {arg}{suffix}')
    py_lines.append(')')
    py_lines.append(f'self.add_widget({widget_name})')
    py_lines.append('')
    
    return py_lines

def get_import_for_widget(widget):
    """Gibt den Import-Statement für ein Widget zurück"""
    widget_type = widget.__class__.__name__
    if widget_type.startswith('Draggable'):
        widget_type = widget_type[9:]  # Entferne 'Draggable' Prefix
    
    import_map = {
        'Button': 'from kivy.uix.button import Button',
        'Label': 'from kivy.uix.label import Label',
        'Slider': 'from kivy.uix.slider import Slider',
        'TextInput': 'from kivy.uix.textinput import TextInput',
        'CheckBox': 'from kivy.uix.checkbox import CheckBox',
        'ProgressBar': 'from kivy.uix.progressbar import ProgressBar'
    }
    
    return import_map.get(widget_type)

if __name__ == "__main__":
    # Test der Export-Funktionen
    class MockWidget:
        def __init__(self, widget_type, x=100, y=100, width=100, height=50, **kwargs):
            self.__class__.__name__ = f'Draggable{widget_type}'
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    class MockWidgetArea:
        def __init__(self):
            self.children = [
                MockWidget('Button', text='Test Button', x=50, y=200),
                MockWidget('Label', text='Test Label', x=200, y=200),
                MockWidget('Slider', x=50, y=100, width=150, min=0, max=100, value=50)
            ]
    
    mock_area = MockWidgetArea()
    export_to_kv(mock_area, 'test_export.kv')
    export_to_py(mock_area, 'test_export.py')
    print("Test-Export abgeschlossen!")
