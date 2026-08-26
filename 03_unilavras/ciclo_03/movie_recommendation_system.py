# Nome: Kaique Junior da Silva Oliveira
# Exercício 4: Sistema de Recomendação de Filmes e Séries - Ciclo III

# Dicionários

categorias = {
    1: "ação",
    2: "comédia",
    3: "drama",
    4: "terror",
    5: "romance",
    6: "suspense",
}

recomendacoes = {
    1: ["John Wick", "Matrix", "Gladiador"],
    2: ["As Branquelas", "Se Beber, Não Case!", "Superbad"],
    3: ["O Poderoso Chefão", "Interstellar", "À Procura da Felicidade"],
    4: ["O Iluminado", "Invocação do Mal", "Hereditário"],
    5: ["Orgulho e Preconceito", "Como Se Fosse a Primeira Vez", "La La Land"],
    6: ["O Sexto Sentido", "Garota Exemplar", "Os Outros"]
}

# Loop Principal
while True:
    print("--- Recomendação de Filmes ---\n")

    for num, categoria in categorias.items():
        print(f"({num}) - {categoria}")

    try:
        opcao = int(input("\nDigite o número da categoria: "))

        if opcao not in categorias.keys():
            print("ERRO! Não existe essa categoria, digite novamente\n")
            continue

    except ValueError:
        print("ERRO! Digite uma opção válida.")
        continue

    match opcao:
        case 1 | 2 | 3 | 4 | 5 | 6:
            print(f"\nRecomendações de {categorias[opcao].title()}: {', '.join(recomendacoes[opcao])}")
        case _:
            print("Opção inválida.")
    break
