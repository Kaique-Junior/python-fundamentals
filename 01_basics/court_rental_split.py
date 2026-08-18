import time

# Ocasiões Específicas
# Foram 2 horas de quadra, porém uma pessoa jogou apenas em 1 horário e vai ajudar a pagar apenas naquele horário.
# Pedir por horário jogado a quantidade de pessoas em tal horário.

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
def pedir_confirmacao(prompt):
    confirmacao = input(f"{prompt}. Digite 'Y' ou 'y' para confirmar e 'N' ou 'n' para negar:")
    if confirmacao == "Y" or confirmacao == "y":
        return True
    elif confirmacao == "N" or confirmacao == "n":
        return False
    else:
        print("Confirmação incorreta, digite 'Y' ou 'y' para confirmar e 'N' ou 'n' para negar")
        pedir_confirmacao(prompt)

 
# 1.2 Criação de Def para Menus

def menu(titulo, prompt1, prompt2):
    print("")
    print(f"{titulo}")
    print("")
    print(f"(1) {prompt1}.")
    print(f"(2) {prompt2}.")
    print("")
    return pedir_numero("Digite o número correspondente a sua escolha", int, 1, 2)
    

# 1.3 Def Calculador Normal / Usado quando não há casos específicos na divisão de horas jogada por pessoa
def calculadora_normal(total_participantes, horas_alugada, valor_hora):
    return valor_hora * horas_alugada / total_participantes
    
# 1.4 Def Calculador Específico / Usado quando há casos específicos na divisao de horas jogada por pessoa

def calculadora_especifica(total_participantes, participantes_1hora, horas_alugada, valor_hora):
        valor_participantes_hora1 = valor_hora / (total_participantes - participantes_1hora) 
        valor_participantes_hora2 = valor_hora / total_participantes 

        valor_participantes_horas_totais = valor_participantes_hora1 + valor_participantes_hora2
        valor_participantes_1hora = valor_participantes_hora2

        print("")
        print("Os", total_participantes - participantes_1hora, "participantes que jogaram as", horas_alugada, "horas totais pagam: R$", valor_participantes_horas_totais)
        print("Os", participantes_1hora, "participantes que jogaram apenas 1 horário pagam: R$", valor_participantes_1hora)
        print("Soma de todos os participantes R$:", valor_participantes_horas_totais * (total_participantes - participantes_1hora) + valor_participantes_1hora * participantes_1hora)
        print("")

# 2. Fluxo Principal

while True:
    escolha = menu("MENU PRINCIPAL", "para inserir valor fixo por hora. (Recomendado sempre que executar esse arquivo)", "para calcular o valor dividido para cada pessoa") 

    # MENU VALOR FIXO POR HORA
    if escolha == 1:

        if valor_hora >= 1:
            print("O Valor está definido como R$", valor_hora)
            confirmacao = pedir_confirmacao("Deseja redefinir o valor?")

            if confirmacao == True:
                valor_hora = pedir_numero("Defina o valor fixo por hora", float, 1, 1000)
                print("O valor fixo foi definido para R$", valor_hora)
                print("Voltando para o Menu...")
                time.sleep(1)
            elif confirmacao == False:
                print("Voltando para Menu...")
                time.sleep(1)
        else:
            print("Não há um valor por hora definido ainda...")
            valor_hora = pedir_numero("Defina o valor fixo por hora", float, 1, 1000)
            time.sleep(1)

    # MENU CALCULADORAS
    if escolha == 2:
        escolha = menu("Qual Calculadora deseja Utilizar?", "Calculadora Normal -- Utilize quando todos os participantes jogaram em todas as horas marcadas.", "Calculadora Específica -- Utilize quando há a condição de ter um ou mais participantes que jogaram apenas em um dos horários -- Exemplo: Quadra alugada para 2 horas, uma pessoa jogou apenas 1 hora")

        # Calculadora Normal
        if escolha == 1:
            total_participantes = pedir_numero("Quantos Participantes no total?", int, 1, 100)
            horas_alugadas = pedir_numero("Quantas Horas Alugada?", int, 1, 24)

            if valor_hora < 1:
                print("Não há um valor por hora definido ainda...")
                valor_hora = pedir_numero("Defina o valor fixo por hora", float, 1, 1000)
                print("O valor fixo por hora foi definido para R$", valor_hora)
                time.sleep(1)

            valor_dividido = calculadora_normal(total_participantes, horas_alugadas, valor_hora)

            print("")
            print("O valor total foi de: R$", valor_hora * horas_alugadas)
            print("Cada pessoa deve pagar: R$", valor_dividido)
            print("")
            time.sleep(5)

        # Calculadora Específica
        if escolha == 2:
            total_participantes = pedir_numero("Quantos Participantes no total", int, 1, 100)
            participantes_1h = pedir_numero("Quantos Participantes Jogaram apenas 1 hora?", int, 1, 100)
            horas_alugadas = pedir_numero("Quantas Horas Alugada", int, 1, 24)

            if valor_hora < 1:
                print("Não há um valor por hora definido ainda...")
                valor_hora = pedir_numero("Defina o valor fixo por hora", float, 1, 1000)
                print("O valor fixo por hora foi definido para R$", valor_hora)
                time.sleep(1)

            print("")
            print("O valor total foi de: R$", valor_hora * horas_alugadas)
            calculadora_especifica(total_participantes, participantes_1h, horas_alugadas, valor_hora)

            time.sleep(5)