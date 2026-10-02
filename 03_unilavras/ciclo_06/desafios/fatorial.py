# Kaique Junior da Silva Oliveira

def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    
    total = 1
    for i in range(2, numero + 1):
        total *= i
        
    return total
        

numero = int(input('Digite o número que quer calcular o fatorial (Escolha números maiores que 1): '))

total = calcular_fatorial(numero)

print(f'\nCalculo do fatorial {numero}! deu o total de: {total}')