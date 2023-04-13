def separate_digits_str(number_str):
    digits_str = list(number_str)
    return digits_str

def ask_base():
    while True:
        print("1 - Decimal | 2 - Binária | 3 - Octal | 4 - Hexadecimal")
        base = input("Digite apenas o número da opção correspondente à base do número que você vai digitar: ")
        if base!="1" and base!="2" and base!="3" and base!="4":
            print("Não entendi.")
        else:
            break
    return base

def test_number(number_str, base):
    number_test = False
    if base != "4":
        if number_str.isdigit() == False:
            print("Deve haver algum erro de digitação.")
        else:
            digits_str = separate_digits_str(number_str)
            number_test = True
    else:
        digits_str = separate_digits_str(number_str)
        for i in digits_str:
            if i.isdigit() == False and (i.upper()!='A') and (i.upper()!='B') and (i.upper()!='C') and (i.upper()!='D') and (i.upper()!='E') and (i.upper()!='F'):
                print("Deve haver algum erro de digitação.")
            else:
                number_test = True
    return number_test

def check_base(number_str, base):
    digits_str = separate_digits_str(number_str)
    max_value = 0

    if base == "1":
        max_value = 9
    elif base == "2":
        max_value = 1
    elif base == "3":
        max_value = 7
    
    if base != "4":
        for i in digits_str:
            if int(i) > max_value:
                return False
    #else:
        # So the number is already checked and it is impossible that there is any digit > 9 that is not one of the allowed letters
    
    return True # If everything went ok, return True


def ask_number(base):
    bool = True
    while bool:
       number_str = input("Digite o seu número: ")
       if test_number(number_str, base) == True:
           if check_base(number_str, base) == True:
               bool = False
           else:
               print("O número que digitou não corresponde à base inserida.")
       else:
           print("Este não é um número válido.")
    
    if base == '4':
        number_str = number_str.upper()
    return number_str

def convert_to_dec(number_str, base):
    digits_str = []
    digit = 0
    base_number = 0
    number_dec = 0
    
    if base == "2":
        base_number = 2
    elif base == "3":
        base_number = 8
    
    if base != "4":
        digits_str = separate_digits_str(number_str)
        for i in range(len(digits_str)):
            digit = int(digits_str[i])
            number_dec += digit * (base_number ** (len(digits_str) - 1 - i))

    else:
        base_number = 16
        digits_str = separate_digits_str(number_str)
        for i in range(len(digits_str)):
            if digits_str[i] == 'A':
                digit = 10
            elif digits_str[i] == 'B':
                digit = 11
            elif digits_str[i] == 'C':
                digit = 12
            elif digits_str[i] == 'D':
                digit = 13
            elif digits_str[i] == 'E':
                digit = 14
            elif digits_str[i] == 'F':
                digit = 15
            else:
                digit = int(digits_str[i])

            number_dec += digit * (base_number ** (len(digits_str) - 1 - i))
                   
    return str(number_dec)

def convert_to_specific_base(number_base_dec_str, specifc_base):
    
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
        converted_number_reverse.append(dig_hex)
    else:
        converted_number_reverse.append(div_int)

    converted_number = list(reversed(converted_number_reverse))
    converted_number_str = converted_number_str.join(str(digit) for digit in converted_number)

    return converted_number_str


def convert_to_bases(number_str, base):
    number_dec = ""
    number_bi = ""
    number_oct = ""
    number_hex = ""

    if base == "1":
        number_dec = number_str
        number_bi = convert_to_specific_base(number_dec, 2)
        number_oct = convert_to_specific_base(number_dec, 8)
        number_hex = convert_to_specific_base(number_dec, 16)
    elif base == "2":
        number_dec = convert_to_dec(number_str, base)
        number_bi = number_str
        number_oct = convert_to_specific_base(number_dec, 8)
        number_hex = convert_to_specific_base(number_dec, 16)
    elif base == "3":
        number_dec = convert_to_dec(number_str, base)
        number_bi = convert_to_specific_base(number_dec, 2)
        number_oct = number_str
        number_hex = convert_to_specific_base(number_dec, 16)
    elif base == "4":
        number_dec = convert_to_dec(number_str, base)
        number_bi = convert_to_specific_base(number_dec, 2)
        number_oct = convert_to_specific_base(number_dec, 8)
        number_hex = number_str

    print(number_dec)
    print(number_bi)
    print(number_oct)
    print(number_hex)

print("Este programa apenas aceita número positivos e sem vírgula")
base = ask_base()
number_str = ask_number(base)
convert_to_bases(number_str, base)

