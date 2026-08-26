# Nome: Kaique Junior da Silva Oliveira
# Exercício 3 - Calculadora

# Resolução
# Código desenvolvido para solucionar o problema proposto.

# 1 - Retornar a soma de dois números;
# 2 - Retornar a subtração de dois números;
# 3 - Retornar a multiplicação de dois números;

# Caso o usuário informe outro código de operação - mostrar mensagem de erro (Opção Inválida).

# Uso de um dicionário para caso queira adicionar novas opções de calculo
# Sempre que adicionar opção no dicionário tem que criar uma nova condição na função calcular().
opcoes_calculos = {
    1: "SOMA",
    2: "SUBTRAÇÃO",
    3: "MULTIPLICAÇÃO",
}

# Função do Menu alocado ao dicionário criado. Ou seja, sempre que uma nova opção for adicionada, ele vai printar.
def menu():
    print("------ Menu de Opções ------\n")
    for numero, tipo in opcoes_calculos.items():
        print(f"{numero} - Retornar a {tipo} de dois números\n")
    print("---------------------------\n")

# Função de Calculos para deixar o código mais limpo e entendivel
def calcular(escolha):
    while True:
        print(f"\n{opcoes_calculos[escolha]} DE DOIS NÚMEROS")
        print("IMPORTANTE: Caso o número tenha casas decimais, separe utilizando . \nExemplo: 1.50 \n")

        try: # Verifica se o que foi digitado é realmente um número, se não for printa "ERRO!" e pede para digitar números válidos novamente.
            n1 = float(input("Informe o 1º número: "))
            n2 = float(input("Informe o 2º número: "))

            # Calculo para retornar valor
            if escolha == 1:
                calculo = n1 + n2
            elif escolha == 2:
                calculo = n1 - n2
            elif escolha == 3:
                calculo = n1 * n2
            print(f"\nResultado: {calculo:.2f}\n")

            break # Interrompe o Loop do Calculo
        except ValueError:
            print("ERRO! Digite apenas números válidos!")


# Loop principal
while True:
    menu()
    try: # Verificação da escolha do usuário, não permitindo o uso de caracteres, apenas números.
        escolha = int(input("Digite o número da opção que deseja: "))
    except ValueError:
        print("ERRO! Digite apenas números.")
        continue

    if escolha not in opcoes_calculos.keys(): # Consulta no dicionário se a opção existe (A função ".keys()" é utilizado para retornar os valores que estão atrás de ":")
        print("\nOPÇÃO INVÁLIDA! Digite o digito correspondente a uma opção que exista no menu!\n")
        continue

    calcular(escolha) # Função que vai retornar o resultado da opção escolhida.
    break # Interrompe Loop Principal