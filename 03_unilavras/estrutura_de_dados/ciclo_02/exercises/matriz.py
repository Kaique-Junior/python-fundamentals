# Kaique Junior da Silva Oliveira
# 2º Período

a = []
b = []
c = []

# Montando as matrizes 2x3 A e B
for i in range(4):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Digite o {i+1}º número da matriz {"A" if i < 2 else "B"}: ")))
    
    # Lógica para determinar em qual matriz tem que entrar os dados
    if i < 2:
        a.append(linha)
    else:
        b.append(linha)
    
    print("\n")
    
# Soma das matrizes para formar a matriz C 
for i in range(2):
    linha = []
    for j in range(3):
        linha.append(a[i][j] + b[i][j])
        
    c.append(linha)

print("Matriz A")
for linha in a:
    print(linha)

print("Matriz B")
for linha in b:
    print(linha)

print("Matriz C")
for linha in c:
    print(linha)