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
    return number_str

def convert_to_dec(number_str, base):
    digits_str = []
    base_number = 0
    number_dec = 0
    
    if base == "2":
        base_number = 2
    
    if base != "4":
        digits_str = separate_digits_str(number_str)
        for i in range(len(digits_str)-1):
            number_dec += int(digits_str[i]) * (base_number ** (len(digits_str) - 1 - i))

    return number_dec

def convert_to_bases(number_str, base):
    number_dec = convert_to_dec(number_str, base)
    print(number_dec)

print("Este programa apenas aceita número positivos e sem vírgula")
base = ask_base()
number_str = ask_number(base)
convert_to_bases(number_str, base)

