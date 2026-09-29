# Kaique Junior da Silva Oliveira

# 4! 4x3x2x1
# Todo número fatorial vai até o 1 (Tudo multiplicado por 1 é o número em si, então não é necessário ir até o 1)
# Ex: 4 x 3 x 2

# Passo 1 - Escolhemos o número fatorial
# Passo 2 - Passamos o número por meio de um argumento de uma função
# Passo 3 - Criamos a função para calcular o fatorial

def calcular_fatorial(numero):
    total = numero
    
    for i in range((numero - 1), 1, -1): # número - 1 para definir o ínicio. EX:. numero = 4! | numero - 1 = 3 | começa no 3 e vai até o 2.   
        total = total * i
        print(total)

numero = int(input('Digite o número que quer calcular o fatorial (Escolha números maiores que 2): '))

calcular_fatorial(numero)