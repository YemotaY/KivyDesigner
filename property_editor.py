from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class PropertyEditor(BoxLayout):
    selected_widget = ObjectProperty(None)

    def update_properties(self, widget):
        self.selected_widget = widget
        # Here you would update the property fields

if __name__ == "__main__":
    from kivy.app import App
    from kivy.lang import Builder
    Builder.load_string('''
<PropertyEditor>:
    orientation: 'vertical'
    Label:
        text: 'Eigenschaften'
    # Properties of selected widget will be shown here
''')
    class TestApp(App):
        def build(self):
            return PropertyEditor()
    TestApp().run()
