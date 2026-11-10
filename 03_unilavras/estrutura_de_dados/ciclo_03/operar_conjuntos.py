# Nome: Kaique Junior da Silva Oliveira
# Período: 2º Período

# Conjuntos
# Programa 2: Operações com conjuntos

entrada1 = input("Digite os elementos do conjunto 1 separados por espaço: ")
conjunto1 = set(entrada1.split())

entrada2 = input("Digite os elementos do conjunto 2 separados por espaço: ")
conjunto2 = set(entrada2.split())

print(f"Conjunto 1: {conjunto1}")
print(f"Conjunto 2: {conjunto2}")

print(f"União: {conjunto1.union(conjunto2)}")
print(f"Interseção: {conjunto1.intersection(conjunto2)}")
print(f"Diferença (1 - 2): {conjunto1.difference(conjunto2)}")
print(f"Diferença (2 - 1): {conjunto2.difference(conjunto1)}")
