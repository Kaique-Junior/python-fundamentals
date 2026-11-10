# Nome: Kaique Junior da Silva Oliveira
# Período: 2º Período

# Dicionários
# Programa 2: Contador de Palavras


texto = input('Digite um texto: ')
palavras = texto.lower().split() # transforma o texto em uma lista de palavras, dividindo elas pelo método .split()

contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

for palavra, quantidade in contagem_palavras.items():
    print(f'{palavra}: {quantidade}')