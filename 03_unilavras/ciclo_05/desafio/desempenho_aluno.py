aprovados = 0
reprovados = 0
recuperacao = 0
soma_notas = 0

# For com sequência exata de 10 vezes
for aluno in range(1, 11):
    nota = float(input(f"\nDigite a nota do aluno ({aluno}): "))
    soma_notas += nota # acumulador

    # Uso de if, elif e else para definir se o aluno foi aprovado, reprovado ou se está de recuperação.
    if nota >= 6:
        print(f"\nAluno ({aluno}) | APROVADO!\n")
        aprovados += 1 # contador

    elif nota >= 4 and nota < 6:
        print(f"\nAluno ({aluno}) | RECUPERAÇÃO!\n")
        recuperacao += 1 # contador

    else:
        print(f"\nAluno ({aluno}) | REPROVADO!\n")
        reprovados += 1 # contador

media = soma_notas / aluno # Calculo da média

# Resumo
resumo = f"Aprovados = {aprovados}" + " | " + f"Recuperação = {recuperacao}" + " | " + f"Reprovados = {reprovados}\n"

print("=" * 17 + " RESUMO FINAL " + "=" * 17 + "\n")
print(resumo)
print(f"Média das Notas da Turma = {media:.1f} pts")