# Nome: Kaique Junior da Silva Oliveira
# Exercício 1 - Reajuste Salarial

# Resolução
# Código desenvolvido para solucionar o problema proposto.

# Tabela Salário
# até 600,00 - +30% 
# 600,01 a 1.100,00 - +25%
# 1100,01 a 2.400,00 - +20%
# 2400,01 a 3.550,00 - +15%
# Acima de 3.550,00 - +10%

# Função para ajudar a deixar o código mais limpo
def calcular_ajuste(salario):
    if salario <= 600:
        return salario + 30/100 * salario # porcentagem é a mesma coisa que número dividido por 100 // Também daria para multiplicar direto por 1,n / Exemplo: salario * 1,3. Que seria a mesma coisa que multiplicar por 130% = 30% a mais
    elif salario <= 1100: # O elif só vai funcionar quando o primeiro if for falso e assim por diante.
        return salario + 25/100 * salario
    elif salario <= 2400:
        return salario + 20/100 * salario
    elif salario <= 3550:
        return salario + 15/100 * salario
    elif salario > 3550:
        return salario + 10/100 * salario

# Uso de While para o sistema não crashar quando algo for digitado errado.
# Uso do Try/Except para verificar se o que foi digitado é realmente um número e não crashar o programa.
while True:
    try:
        salario = float(input("Informe o salário: ")) # Float pois o salário pode ter casas decimais.

        if salario < 0: # Caso do Usuário digitar um número negativo
            print("ERRO! O salário não pode ser negativo!\n")
            continue

        print(f"O seu salário é de R$ {salario:.2f}")

        confirm = input("\nVocê digitou o salário correto? (1) para sim e (2) para não: ") # Confirmar se o usuário escreveu o salário corretamente. Caso sim: Volta o salário dele ajustado e quebra o loop. Caso não: Reinicia o Loop.

        if confirm == "1":
            print("\nCalculando seu salário ajustado...")
            print(f"O Salário Ajustado é de: R$ {calcular_ajuste(salario):.2f}") # Calcula e retorna o resultado para o Usuário
            break
        elif confirm == "2":
            print("Certo! Voltando para menu\n")
        else:
            print("ERRO! Digitou um número inválido. Voltando para o menu.\n")

    except ValueError:
        print("ERRO! Digite apenas números.\n")

