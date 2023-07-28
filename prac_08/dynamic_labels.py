from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Bob brown', 'Cat Cyan', 'Oren ochre']

    def build(self):
        layout = BoxLayout(orientation='vertical')
        main_layout = BoxLayout(orientation='vertical')

        for name in self.names:
            label = Label(text=name)
            main_layout.add_widget(label)

        layout.add_widget(main_layout)
        return layout


if __name__ == '__main__':
    DynamicLabelsApp().run()
