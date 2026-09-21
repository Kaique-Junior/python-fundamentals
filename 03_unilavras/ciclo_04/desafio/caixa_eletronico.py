opcoes_menu = { # Uso de Dicionário para ajudar na solução
1: "depósito",
2: "saque",
3: "saldo",
4: "sair",
}

saldo_depositado = 1000 # Váriavel definida pelo enunciado

while True: # Loop True para sempre rodar até que o usuário digite 4 para quebrar o loop
    print("\n=== Caixa-Eletrônico ===")

    for num, opcao in opcoes_menu.items(): # Menu utilizando for para entrar dentro do dicionário
        print(f"{num} - {opcao}")

    try: # Tratamento de ERRO para caso o usuário escreva letras invés de números. (Para não quebrar o programa)
        opcao = int(input("\nOpção: "))
    except ValueError:
        print("\nERRO! Digite apenas números inteiros!")
        continue

    match opcao: # Match Case invés de if para ficar mais organizado a estrutura de decisões.
        case 1:
            deposito = float(input("\nValor do depósito: R$"))
            saldo_depositado += deposito # Adiciona ao saldo
        case 2:
            saque = float(input("\nValor do saque: R$"))
            saldo_depositado -= saque # Tira do Saldo
        case 3:
            print(f"\nSaldo atual: R${saldo_depositado:.2f}")
        case 4:
            print("\nFim das transações!")
            break # Interrompe o loop quando o usuário digitar 4
        case _:
            print("Opção incorreta!")