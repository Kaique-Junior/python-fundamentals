# Nome: Kaique Junior da Silva Oliveira
# Exercício 4 - Cardápio de Lanchonete

# Resolução
# Código desenvolvido para solucionar o problema proposto.

# Lista de Dicionários
cardapio = [
    {"codigo": 100, "nome": "Cachorro quente", "preco": 1.20},
    {"codigo": 101, "nome": "Bauru simples", "preco": 1.30},
    {"codigo": 102, "nome": "Bauru com ovo", "preco": 1.50},
    {"codigo": 103, "nome": "Hambúrguer", "preco": 1.20},
    {"codigo": 104, "nome": "Cheeseburguer", "preco": 1.30},
    {"codigo": 105, "nome": "Refrigerante", "preco": 1.00},
]

# Função do Menu
def menu():
    print("---------------- MENU ----------------")
    print(f"{'NOME':<18} {'CÓDIGO':<10} {'PREÇO'}") # Aprendi sobre as identações
    for item in cardapio: # Vai percorrer por toda a lista com dicionários e realizar o print do menu com os items.
        nome = item["nome"]
        codigo = item["codigo"]
        preco = item["preco"]

        print(f"{nome:<18} {codigo:<10} R${preco:.2f}")

# LOOP PRINCIPAL
while True:
    menu()
    try:
        # Input de Código do Produto + Verificação se o que foi digitado está válido.
        codigo = int(input("\nDigite o código da sua opção: "))

        # Achar dicionário dentro da lista que se refere ao código informado e colocar dentro da variável item_selecionado.
        item_selecionado = None
        for item in cardapio:
            if item["codigo"] == codigo:
                item_selecionado = item # Recebe o dicionário do produto selecionado pelo código.
                break

        if not item_selecionado: # Condição para caso o usuário digite um código que não exista na lista.
            print("\nCÓDIGO INVÁLIDO. Esse código não está no cardápio.")
            continuechanginginto

        # Input de Quantidade + Verificação se o que foi digitado está correto.
        quantidade = int(input("Digite a quantidade desejada: "))

        if quantidade < 1:
            print("\nERRO! Não pode digitar números menores do que 1!")
            continue

    except ValueError:
        print("\nERRO! Digite apenas números inteiros!")
        continue

    # Calculo do Preço do Produto * Quantidade
    print(f"\nVocê selecionou o item: {item_selecionado["nome"].upper()}") # Printa o produto selecionado em letra maiuscula utilizando a função .upper()

    valor_item = item_selecionado["preco"]
    total = valor_item * quantidade

    print(f"\nTotal: R$ {total:.2f}")
    break # Interrompe o loop principal
    