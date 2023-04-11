def ask_number():
    while True:
        number = input("Digite um número natural: ")
        if number.isdigit() == False:
            print("Apenas números naturais, por favor.")
        else:
            break
    print(number)

def ask_base():
    while True:
        print("1 - Decimal | 2 - Binária | 3 - Octal | 4 - Hexadecimal")
        base = input("Digite apenas o número da opção correspondente à base do número que você digitou: ")
        if base!="1" and base!="2" and base!="3" and base!="4":
            print("Não entend. Por favor, digite a apenas o número da base do seu número.")
        else:
            break
    print(base)

ask_number()
ask_base()
