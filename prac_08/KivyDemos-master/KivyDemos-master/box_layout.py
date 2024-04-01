from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')  # Make sure this points to the correct file
        return self.root

    def handle_clear(self):

        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = 'Enter your name'

    def handle_greet(self):
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"


BoxLayoutDemo().run()
