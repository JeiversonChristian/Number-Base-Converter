while True:
    number = input("Digite um número natural: ")
    if number.isdigit() == False:
        print("Apenas números naturais!")
    else:
        break
print(number)