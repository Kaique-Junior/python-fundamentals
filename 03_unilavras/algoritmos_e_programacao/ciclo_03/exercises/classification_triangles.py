# Nome: Kaique Junior da Silva Oliveira
# Exercício 2: Sistema de Classificação de Triângulos

# Loop Principal
while True:
    print("Classificação de Triangulos\n")

    # Entrada de Dados
    try:
        lado1 = float(input("Informe o comprimento do lado 1: "))
        lado2 = float(input("Informe o comprimento do lado 2: "))
        lado3 = float(input("Informe o comprimento do lado 3: "))

        # Verificação se é um Triângulo válido.
        if lado1 > 0 and lado2 > 0 and lado3 > 0 and (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
            print("\nÉ um triângulo!")
        else:
            print("Não é um triângulo válido!")
            break

    except ValueError:
        print("ERRO! Digite números válidos.")
        continue

    # Classificação do Triângulo

    if lado1 == lado2 == lado3:
        print("Esse é um Triângulo Equilátero!")
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        print("Esse é um Triângulo Isósceles")
    else:
        print("Esse é um Triângulo Escaleno")
    break