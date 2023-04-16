# Importing libraries
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Layout and all functions
class MyGridLayout(GridLayout):

    # Creating the layout
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        # Columns number
        self.cols = 1

        # Layout elements
        self.initial_text = "CONVERSOR DE BASES"
        self.add_widget(Label(color=(0,1,0,1),text=self.initial_text, bold=True, font_size='24'))

        self.base_text1 = "1 - Decimal | 2 - Binário | 3 - Octal | 4 - Hexadecimal"
        self.add_widget(Label(text=self.base_text1))

        self.base_text2 = f"Qual é a base do seu número?\n  (APENAS O Nº DA OPÇÃO)"
        self.add_widget(Label(text=self.base_text2))
        self.base_option_str = ""
        self.base_option_str = TextInput(multiline=False, halign="center", size_hint=(0.5, 0.5))
        self.add_widget(self.base_option_str)

        self.number_text = "Digite o seu número:"
        self.add_widget(Label(text=self.number_text))
        self.number_str = ""
        self.number_str = TextInput(multiline=False, halign="center", size_hint=(0.5, 0.5))
        self.add_widget(self.number_str)

        self.submit = Button(text="CONVERTER", background_color=(0, 1, 0, 1))
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

        self.answer1 = Label(text="Decimal:")
        self.add_widget(self.answer1)

        self.answer2 = Label(text="Binário:")
        self.add_widget(self.answer2)

        self.answer3 = Label(text="Octal:")
        self.add_widget(self.answer3)

        self.answer4 = Label(text="Hexadecimal:")
        self.add_widget(self.answer4)

    # Check if the text of the base option is valid    
    def check_base_text(self, base_option_str):
        base = base_option_str
        if base!="1" and base!="2" and base!="3" and base!="4":
            return False
        else:
            return True

    # Separate the digits of the number in a vetor      
    def separate_digits_str(self, number_str):
        digits_str = list(number_str)
        return digits_str

    # Check if the text of the number is valid
    def check_number_text(self, number_str):
        # number_test = False
        digits_str = self.separate_digits_str(number_str)
        for i in digits_str:
            if i.isdigit() == True:
                if int(i) < 0:
                    return False
            if i.isdigit() == False and (i.upper()!='A') and (i.upper()!='B') and (i.upper()!='C') and (i.upper()!='D') and (i.upper()!='E') and (i.upper()!='F'):
                return False
            else:
                return True
        # return number_test
    
    # Check if the number matches with its base
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
    
    # Convert the number to the decimal base
    def convert_to_dec(self, number_str, base_option_str):
        base = base_option_str
        digits_str = []
        digit = 0
        base_number = 0
        number_dec = 0
    
        if base == "2":
            base_number = 2
        elif base == "3":
            base_number = 8
    
        if base != "4":
            digits_str = self.separate_digits_str(number_str)
            for i in range(len(digits_str)):
                digit = int(digits_str[i])
                number_dec += digit * (base_number ** (len(digits_str) - 1 - i))

        else:
            base_number = 16
            digits_str = self.separate_digits_str(number_str)
            for i in range(len(digits_str)):

                if digits_str[i].upper() == 'A':
                    digit = 10
                elif digits_str[i].upper() == 'B':
                    digit = 11
                elif digits_str[i].upper() == 'C':
                    digit = 12
                elif digits_str[i].upper() == 'D':
                    digit = 13
                elif digits_str[i].upper() == 'E':
                    digit = 14
                elif digits_str[i].upper() == 'F':
                    digit = 15
                else:
                    digit = int(digits_str[i])

                number_dec += digit * (base_number ** (len(digits_str) - 1 - i))
                   
        return str(number_dec)
    
    # Convert a decimal number to a specific base
    def convert_to_specific_base(self, number_base_dec_str, specifc_base):
    
        converted_number_str = ''
        number_base_dec_int = int(number_base_dec_str)
        div_rest = 0
        div_int = specifc_base + 1
        converted_number_reverse = []
        converted_number= []

        dig_hex = ''

        while div_int >= specifc_base:
            div_rest = number_base_dec_int % specifc_base
            if div_rest > 9:
                if div_rest == 10:
                    dig_hex = 'A'
                elif div_rest == 11:
                    dig_hex = 'B'
                elif div_rest == 12:
                    dig_hex = 'C'
                elif div_rest == 13:
                    dig_hex = 'D'
                elif div_rest == 14:
                    dig_hex = 'E'
                else:
                    dig_hex = 'F'
                converted_number_reverse.append(dig_hex)
            else:    
                converted_number_reverse.append(div_rest)
            div_int = number_base_dec_int // specifc_base
            number_base_dec_int = div_int
        if div_int > 9:
            if div_int == 10:
                dig_hex = 'A'
            elif div_int == 11:
                dig_hex = 'B'
            elif div_int == 12:
                dig_hex = 'C'
            elif div_int == 13:
                dig_hex = 'D'
            elif div_int == 14:
                dig_hex = 'E'
            else:
                dig_hex = 'F'
            converted_number_reverse.append(dig_hex)
        else:
            converted_number_reverse.append(div_int)

        converted_number = list(reversed(converted_number_reverse))
        converted_number_str = converted_number_str.join(str(digit) for digit in converted_number)

        return converted_number_str
    
    # Convert a number to all available bases
    def convert_to_bases(self, number_str, base_option_str):
        base = base_option_str
        number_dec = ""
        number_bi = ""
        number_oct = ""
        number_hex = ""

        if base == "1":
            number_dec = number_str
            number_bi = self.convert_to_specific_base(number_dec, 2)
            number_oct = self.convert_to_specific_base(number_dec, 8)
            number_hex = self.convert_to_specific_base(number_dec, 16)
        elif base == "2":
            number_dec = self.convert_to_dec(number_str, base)
            number_bi = number_str
            number_oct = self.convert_to_specific_base(number_dec, 8)
            number_hex = self.convert_to_specific_base(number_dec, 16)
        elif base == "3":
            number_dec = self.convert_to_dec(number_str, base)
            number_bi = self.convert_to_specific_base(number_dec, 2)
            number_oct = number_str
            number_hex = self.convert_to_specific_base(number_dec, 16)
        elif base == "4":
            number_dec = self.convert_to_dec(number_str, base)
            number_bi = self.convert_to_specific_base(number_dec, 2)
            number_oct = self.convert_to_specific_base(number_dec, 8)
            number_hex = number_str

        self.answer1.text = f"Decimal: {number_dec}"
        self.answer2.text = f"Binário: {number_bi}"
        self.answer3.text = f"Octal: {number_oct}"
        self.answer4.text = f"Hexadecimal: {number_hex}"

    # Active when press the button
    def press(self, instance):

        if self.base_option_str.text == "" or self.number_str.text == "":
            self.answer1.text = "FALTA"
            self.answer2.text = "base"
            self.answer3.text = "e/ou"
            self.answer4.text = "número"
        else:
        
            base_option_str = self.base_option_str.text
            number_str = self.number_str.text

            base_text_test = self.check_base_text(base_option_str)
            number_text_test = self.check_number_text(number_str)
            match_base_number_teste = self.match_base_number(number_str, base_option_str)

            if base_text_test == False:
                self.answer1.text = "Base inválida!"
                self.answer2.text = "Digite apenas"
                self.answer3.text = "o nº da opção."
                self.answer4.text = ""
            elif base_text_test == True:
                if number_text_test == False:
                    self.answer1.text = "Número inválido"
                    self.answer2.text = "verifique!"
                    self.answer3.text = "Não negativos!"
                    self.answer4.text = "Sem vírgula!"
                elif match_base_number_teste == False:
                    self.answer1.text = "O seu número"
                    self.answer2.text = "não é da base"
                    self.answer3.text = "que você indicou."
                    self.answer4.text = "Verifique!"
                else:
                    self.convert_to_bases(number_str, base_option_str)

# The application
class MyApp(App):

    # Build and return the layout
    def build(self):
        return MyGridLayout()

# Run the application    
if __name__ == '__main__':
    MyApp().run()