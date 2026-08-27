# Nome: Kaique Junior da Silva Oliveira
# Exercício 1: Calculadora de Bônus Salarial - Ciclo III

# Dicionário
avaliacao_desempenho = {
    1: "Bom!",
    2: "Ótimo!",
    3: "Excelente!",
}

# Funções

# Função para pedir números
def pedir_numero(prompt, tipodado):
    while True:
        try:
            return tipodado(input(f"{prompt}: "))
        except ValueError:
            print("ERRO! Digite apenas números!")
            continue

# Loop Principal

while True:
    # Entrada de Dados
    print("--- Calculadora de Bônus Salarial ---\n")

    print("ATENÇÃO! Se o salário tiver números após a virgula, separe eles usando o . invés da virgula.")
    salario_atual = pedir_numero("Informe o salário do funcionário", float)
    tempo_servico = pedir_numero("Informe o tempo de serviços em anos do funcionário", int)
    print("\n")

    # Loop Secundário para tratamento de falhas, caso ocorra.
    while True:
        print("\nAvalie seu Funcionário")
        print("(1) Bom")
        print("(2) Ótimo")
        print("(3) Excelente\n")

        avaliacao = pedir_numero("Informe o nível de desempenho do funcionário", int)

        if avaliacao not in avaliacao_desempenho.keys():
            print("\nERRO! Digite o número corresponde que exista na tabela!\n")
            continue
        else:
            print(f"O seu funcionário foi avaliado em: {avaliacao_desempenho[avaliacao].upper()}\n")
            break # Interrompe Loop Secundário

    print("--- Tabela de Bônus ---\n")

    print("--- Tempo de Serviço ---")
    print("Menor que 5 anos, não há bônus!")
    print("De 5 a 10 anos, 5% de bônus do salário!")
    print("Maior que 10 anos, 10% de bônus do salário!\n")

    print("--- Desempenho ---")
    print("BOM = Bônus de 10% do salário")
    print("ÓTIMO = Bônus de 15% do salário")
    print("EXCELENTE = Bônus de 20% do salário\n")

    # Processamento dos Dados

    # Bônus Tempo de Serviço

    if tempo_servico < 5:
        print("Não há bônus de tempo de serviço!")
        bonus_tempo = 0
    elif 5 <= tempo_servico <= 10:
        print("Há um bônus de 5% do salário")
        bonus_tempo = 5
    elif tempo_servico > 10:
        print("Há um bônus de 10% do salário")
        bonus_tempo = 10

    # Bônus Desempenho

    if avaliacao == 1:
        print("Bônus de 10% do salário")
        bonus_avaliacao = 10
    elif avaliacao == 2:
        print("Bônus de 15% do salário")
        bonus_avaliacao = 15
    elif avaliacao == 3:
        print("Bônus de 20% do salário")
        bonus_avaliacao = 20

    # Aumento do Salário

    bonus_total = (bonus_tempo + bonus_avaliacao)
    valor_bonus = salario_atual * (bonus_total / 100)
    salario_novo = salario_atual + valor_bonus

    print(f"\nValor do bônus total recebido: R${valor_bonus:.2f}")
    print(f"O novo salário com um bônus de {bonus_total}% ficou: R${salario_novo:.2f}\n")
    break # Interrompe Loop Principal