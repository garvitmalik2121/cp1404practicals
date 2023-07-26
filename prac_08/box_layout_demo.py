from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root
    def handle_greet(self):
        print('greet')
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        # This method is called when the "Clear" button is pressed.
        # It will reset the TextInput and the output_label to blank.
        input_widget = self.root.ids.input_name
        output_widget = self.root.ids.output_label
        input_widget.text = ""
        output_widget.text = ""

BoxLayoutDemo().run()