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

        self.answer = Label(text="")
        self.add_widget(self.answer)
    
    def check_base_text(self, base_option_str):
        base = base_option_str
        if base!="1" and base!="2" and base!="3" and base!="4":
            return False
        else:
            return True
        
    def separate_digits_str(self, number_str):
        digits_str = list(number_str)
        return digits_str

    def check_number_text(self, number_str):
        number_test = False
        digits_str = self.separate_digits_str(number_str)
        for i in digits_str:
            if i.isdigit() == False and (i.upper()!='A') and (i.upper()!='B') and (i.upper()!='C') and (i.upper()!='D') and (i.upper()!='E') and (i.upper()!='F'):
                number_test = False
            else:
                number_test = True
        return number_test
    
    def match_base_number(self, number_str, base_option_str):
        base = base_option_str
        digits_str = self.separate_digits_str(number_str)
        max_value = 0

        if base == "1":
            max_value = 9
        elif base == "2":
            max_value = 1
        elif base == "3":
            max_value = 7
    
        if base != "4":
            for i in digits_str:
                if i.isdigit() == False:
                    return False
                elif int(i) > max_value:
                    return False
        #else:
            # So the number is already checked and it is impossible that there is any digit > 9 that is not one of the allowed letters
    
        return True # If everything went ok, return True


    def press(self, instance):
        
        base_option_str = self.base_option_str.text
        number_str = self.number_str.text

        base_text_test = self.check_base_text(base_option_str)
        number_text_test = self.check_number_text(number_str)
        match_base_number_teste = self.match_base_number(number_str, base_option_str)

        if base_text_test == False:
            self.answer.text = "Base inválida - digite o nº da opção."
        elif base_text_test == True:
            if number_text_test == False:
                self.answer.text = "Número inválido - verifique"
            elif match_base_number_teste == False:
                self.answer.text = "O seu número não é da base que você indicou."
            else:
                self.answer.text = "Tudo ok"

        #self.add_widget(Label(text=f"Base: {base_option_str} | Número: {number_str}"))

class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    MyApp().run()