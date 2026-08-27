while True:
    try:
        num1 = int(input("\nInforme o primeiro número: "))
        num2 =  int(input("Informe o segundo número: "))
        break
    except ValueError:
        print("\nERRO! Digite apenas números inteiros\n")
        continue

if num1 > num2:
    print("\nO primeiro número é o maior!")
elif num2 > num1:
    print("\nO segundo número é o maior!")
else:
    print("\nOs números são iguais!")
