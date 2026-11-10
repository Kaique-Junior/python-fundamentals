# Nome: Kaique Junior da Silva Oliveira
# Exercício 2 - Metódos de Pagamento

# Resolução
# Código desenvolvido para solucionar o problema proposto.

# Pagamentos à vista tem desconto de 5%. Pagamento parcelado terá um acréscimo de 8% (Não específicado no exercício 2 se é a cada parcela, então vou presumir que vai ter apenas um acréscimo de 8% no valor total)

# OBS 01: Caso o Usuário escolha o pagamento a prazo, você deverá solicitar a quantidade de parcelas.
# OBS 2: Caso ele escolha uma opção diferente de 1 ou 2, mostre erro.
# OBS 3: Caso ele informe um número de parcelas menor que 1, mostre erro.

# Fazer um dicionário fica mais fácil de verificar o preço das parcelas.

regras_parcelamento = {
    1: 1.0,
    2: 2.0,
    3: 10.0,
    4: 20.0,
    5: 30.0,
    6: 40.0,
    7: 50.0,
    8: 60.0,
    9: 70.0,
    10: 80.0,
    11: 90.0,
    12: 100.0,
}


# Função para deixar o código limpo e printar a tabela de parcelamento para o Usuário

# Antes de pensar em criar um dicionário para salvar os dados de cada parcela, fiz o menu com vários prints.

# print("\n----- Tabela de Parcelamento -----")
# print("1 Parcela | Compra mínima | R$1,00")
# print("2 Parcelas | Compra mínima | R$2,00")
# print("3 Parcelas | Compra mínima | R$10,00")
# print("4 Parcelas | Compra mínima | R$20,00")
# print("5 Parcelas | Compra mínima | R$30,00")
# print("6 Parcelas | Compra mínima | R$40,00")
# print("7 Parcelas | Compra mínima | R$50,00")
# print("8 Parcelas | Compra mínima | R$60,00")
# print("9 Parcelas | Compra mínima | R$70,00")
# print("10 Parcelas | Compra mínima | R$80,00")
# print("11 Parcelas | Compra mínima | R$90,00")
# print("12 Parcelas | Compra mínima | R$100,00")
# print("--- -------------------------- ---\n")

# Função nova utilizando for para passar dentro do dicionário e imprimir a tabela.

def tabela_parcelamento():
    print("\n----- Tabela de Parcelamento -----")
    for parcelas, minimo in regras_parcelamento.items(): # Vai passar por todos os items do dicionário puxando o Nº parcelas e o valor minimo de cada parcela.
        print(f"{parcelas} Parcelas | Compra mínima | R${minimo:.2f}")
    print("--- -------------------------- ---\n")
        
# Loop Principal
while True:
    try:
        valor_compra = float(input("Informe o valor da compra: R$")) # Pede o valor da compra e após isso verifica se o valor não é menor que 0. Se for, repete o input.
        if valor_compra <= 0:
            print("ERRO! Digite um valor maior do que 0!\n")
            continue

        tipo_pagamento = input("Informe o tipo de pagamento (1 - À vista (5% de desconto) ou 2 - Parcelado (8% de acréscimo)):")

        if tipo_pagamento not in ["1", "2"]: # Para caso o usuário colocar algo diferente de opção "1" ou "2", retorne um ERRO sem quebrar o código.
            print("ERRO! Opção inválida. Digite 1 ou 2\n")
            continue

        # Pagamento à Vista
        if tipo_pagamento == "1":
            if valor_compra >= 2: # Condição para ter desconto apenas em compras acima de R$2,00
                print(f"\nO valor a ser pago com desconto é de: R${valor_compra * 0.95:.2f}\n")
            else:
                print("\nO desconto apenas se aplica a compras com o valor maior ou igual a R$2,00")
                print(f"Valor a pagar: R${valor_compra:.2f}\n")
            break # Interrompe o loop principal

        # Pagamento a Prazo (Parcelado)
        # Pensei no caso do cliente comprar algo muito barato e querer parcelar em muitas parcelas. Por isso vou fazer uma tabela para o usuário saber o quanto pode parcelar.
        if tipo_pagamento == "2": 
            tabela_parcelamento()

            # Loop Parcelamento

            while True:
                try:
                    quantidade_parcelas = int(input("Informe a quantidade de parcelas (1 a 12): "))

                    # Verificação sobre se a parcela não é menor que 1 ou maior que 12
                    if quantidade_parcelas < 1 or quantidade_parcelas > 12:
                        print("ERRO! Número de parcelas deve ser entre 1 e 12.\n")
                        continue

                    # Valida se o valor da compra atinge o mínimo daquela parcela específica

                    valor_minimo = regras_parcelamento[quantidade_parcelas] # Uso do dicionário regras_parcelamentos para a verificação.

                    if valor_compra < valor_minimo: # Condição para caso o valor não seja correspondente ao quantidade de parcelas que pode dividir.
                        print(f"ERRO! Para parcelar em {quantidade_parcelas}x, o valor mínimo da compra deve ser R${valor_minimo:.2f}\n")
                        continue
                    
                    # Se passou por todas as validações, sai do loop interno de parcelas
                    break

                except ValueError:
                    print("ERRO! Digite um número inteiro válido de parcelas.")

            # Cálculo final com o acréscimo de 8%
            valor_com_acrescimo = valor_compra * 1.08

            # Cálculo de valor por parcela
            valor_parcela = valor_com_acrescimo / quantidade_parcelas

            # Retorna valor para o Usuário.
            print(f"\nValor total parcelado (8% acréscimo): R${valor_com_acrescimo:.2f}")
            print(f"Parcelado em {quantidade_parcelas}x de R${valor_parcela:.2f}\n")
            break # Interrompe o loop principal
        
    except ValueError:
        print("ERRO! Digite apenas números.")