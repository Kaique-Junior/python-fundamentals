# Ocasiões Específicas
# Foram 2 horas de quadra, porém uma pessoa jogou apenas em 1 horário e vai ajudar a pagar apenas naquele horário.
# Pedir por horário jogado a quantidade de pessoas em tal horário.

valor_hora = 0

# 1. Criação de Def facilitadoras

# 1.1 Criação de Def para pedir_número sem crashar quando colocar letra ou um número inválido.
def pedir_numero(prompt, tipo_dado, minimo, maximo):
    try:
        number = tipo_dado(input(f"{prompt}: "))
        if minimo <= number <= maximo:
            return number
        else:
            print(f"Por favor digite apenas números entre {minimo} e {maximo}")
    except ValueError:
        print(f"Por favor digite apenas números válidos entre {minimo} e {maximo}!")

# 1.1.1 Def pedir confirmação Y ou N
def pedir_confirmacao():
    pass
 
# 1.2 Criação de Def para Menu

def menu():
    print("")
    print("Calculadora de Divisão de Quadra Alugada")
    print("")
    print("(1) para inserir valor fixo por hora. (Recomendado sempre que executar esse arquivo)")
    print("(2) para calcular o valor dividido para cada pessoa")
    print("")

# 1.3 Def Calculador Normal / Usado quando não há casos específicos na divisão de horas jogada por pessoa

# 1.4 Def Calculador Específico / Usado quando há casos específicos na divisao de horas jogada por pessoa

# 2. Fluxo Principal

while True:
    menu() # Chama o menu

    # Início da Lógica a ser criada
    escolha = pedir_numero("Digite o número correspondente", int, 1, 2)

    # MENU VALOR FIXO POR HORA
    if escolha == 1:
        if valor_hora >= 1:
            print("O Valor está definido como R$", valor_hora)
            # Def de Confirmação faltando ser criado, porém irá chamar essa def e depois verificar com um if se foi y ou n para ter um respectivo caminho.   
        else:
            print("Não há um valor por hora definido ainda...")
            valor_hora = pedir_numero("Defina o valor fixo por hora", float, 1, 1000)

    # MENU CALCULADORAS