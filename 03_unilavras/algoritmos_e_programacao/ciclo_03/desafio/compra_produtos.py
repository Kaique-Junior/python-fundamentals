# Desafio 4

while True:
    try:
        print("Tabela de Preços / grama")
        print("Código produtos - 1, 2, 3 e 4 - R$0.10 por grama")
        print("Código produtos - 5, 6 e 7 - R$0.25 por grama")
        print("Código produtos - 8, 9 e 10 - R$0.35 por grama\n")

        codigo = int(input("Informe o código do produto: "))

        # Match para verificar onde o código do produto entra na tabela de preços
        match codigo:
            case 1 | 2 | 3 | 4:
                preco_g = 0.1
            case 5 | 6 | 7:
                preco_g = 0.25
            case 8 | 9 | 10:
                preco_g = 0.35
            case _:
                print("\nERRO! Código inválido\n")
                continue

        while True: # Loop Secundário para Tratamento de Erro
            try:
                print("\nCaso o número seja em decimal utilize . para separar (Exemplo: 1.5)")
                peso_kg = float(input("Informe o peso em quilos do produto: "))

                print("\nTabela de Código do País de Origem")
                print("(1) 0% imposto")
                print("(2) 15% imposto")
                print("(3) 25% imposto\n")

                origem = int(input("Digite o código do país de origem: "))

                # Match para verificar qual imposto vai ser cobrado
                match origem:
                    case 1:
                        imposto = 0
                        break # Interrompe o Loop Secundário
                    case 2:
                        imposto = 15
                        break # Interrompe o Loop Secundário
                    case 3:
                        imposto = 25
                        break # Interrompe o Loop Secundário
                    case _:
                        print("\nERRO! Código de país inválido.\n")
                        continue

            except ValueError:
                print("\nERRO! Digite apenas números\n")
        break # Interrompe o Loop Principal
    except ValueError:
        print("\nERRO! Digite apenas números\n")
        continue

peso_g = peso_kg * 1000
preco_total = peso_g * preco_g
valor_imposto = preco_total * (imposto / 100)
valor_total = preco_total + valor_imposto

print(f"\nPeso em gramas: {peso_g}g")
print(f"Preço total do produto: R${preco_total:.2f}")
print(f"Valor do imposto: R${valor_imposto:.2f}")
print(f"Valor total com imposto: R${valor_total:.2f}")

