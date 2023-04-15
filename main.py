import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1

        self.base_text1 = "1 - Decimal | 2 - Binária | 3 - Octal | 4 - Hexadecimal"
        self.add_widget(Label(text=self.base_text1))

        self.base_text2 = "Qual é a base do seu número? (APENAS O Nº DA OPÇÃO)"
        self.add_widget(Label(text=self.base_text2))
        self.base_option_str = TextInput(multiline=False)
        self.add_widget(self.base_option_str)

        self.number_text = "Digite o seu número:"
        self.add_widget(Label(text=self.number_text))
        self.number_str = TextInput(multiline=False)
        self.add_widget(self.number_str)

        self.submit = Button(text="Submit", font_size=32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        base_option_str = self.base_option_str.text
        number_str = self.number_str.text

        self.add_widget(Label(text=f"Base: {base_option_str} | Número: {number_str}"))

class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()