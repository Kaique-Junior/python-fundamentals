# Nome: Kaique Junior da Silva Oliveira
# Período: 2º Período

# Conjuntos
# Programa 1: Remover Duplicatas

entrada = input('Digite uma lista de números separados por espaço: ').split()
lista_original = [int(x) for x in entrada]

vistos = set()
lista_sem_duplicatas = []

for numero in lista_original:
    if numero not in vistos:
        lista_sem_duplicatas.append(numero)
        vistos.add(numero)

print(f'Lista original: {lista_original}')
print(f'Lista sem duplicatas: {lista_sem_duplicatas}')