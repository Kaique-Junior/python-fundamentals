print("DOM  SEG  TER  QUA  QUI  SEX  SAB")
# Colunas: DOM=0, SEG=1, TER=2, QUA=3, QUI=4, SEX=5, SAB=6

linha = "               " # 15 de Espaço para começar a primeira semana na Quarta-feira
coluna = 3  # Primeira semana começa na Quarta-feira

for dia in range(1, 32): # percorre os 31 dias do mês

    # Caso o número ter apenas 1 digito, precisa de 2 espaços antes, se não apenas 1 espaço.
    if dia < 10:
        linha = linha + "  " + str(dia) + "  "
    else:
        linha = linha + " " + str(dia) + "  "

    coluna = coluna + 1

    # Quando a coluna chegar a 7 (Após Sábado), imprime a linha com os dias referente aos dias da semana e limpa as váriaveis para começar nova semana.
    if coluna == 7:
        print(linha) 
        linha = ""
        coluna = 0

# Para imprimir a última semana que tem apenas 6 colunas.
if linha != "":
    print(linha)