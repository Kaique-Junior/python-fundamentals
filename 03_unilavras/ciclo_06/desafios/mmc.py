# Kaique Junior da Silva Oliveira

def calcular_mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calcular_mmc(a, b):
    return (a * b) // calcular_mdc(a, b)

# Entrada
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

# Saída
print(calcular_mmc(a, b))