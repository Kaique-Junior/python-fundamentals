import time

# // Sistema de Cadastro de Alunos e Notas
## // LISTAS
alunos = []

## // FUNÇÕES PRINCIPAIS
def pedir_numero(prompt, minimo, maximo, tipo_dado):
    
        while True:
            try:
                valor = tipo_dado((input(prompt)))
                if minimo <= valor <= maximo:
                    return valor
                else:
                    print(f"ERRO! O valor está fora do valor minimo {minimo} e o máximo {maximo}, tente novamente!")
            except ValueError:
                print("ERRO! Digite um valor numérico válido,  tente novamente!")
                
def menu():
    print("SISTEMA DE CADASTRO DE ALUNOS E NOTAS")
    print("Digite (1) para ver as informações dos alunos")
    print("Digite (2) para cadastrar informações de novos alunos")

    opcao_escolhida = pedir_numero("Digite o número correspondente: ", 1, 2, int)
    if opcao_escolhida == 1:
        if not alunos:
            print("\nNenhum Aluno Cadastrado Ainda!")
        else:
            print("\n--- LISTA DE ALUNOS ---")
            for aluno in alunos:
                print(f"Nome: {aluno['nome']} | Média: {aluno['media']:.1f} | Status: {aluno['status']}")
        time.sleep(5)
    elif opcao_escolhida == 2:
        numero_cadastro = pedir_numero("Digite o número de alunos a ser cadastrados(minimo: 1 e máximo: 5 por vez): ", 1, 5, int)
        for i in range(numero_cadastro):
            nome = input("Escreva o nome do Aluno:")
            nota1 = pedir_numero("Digite a nota 1 do aluno(0 a 10):", 0, 10, float)
            nota2 = pedir_numero("Digite a nota 2 do aluno(0 a 10):", 0, 10, float)
            media = (float(nota1) + float(nota2)) / 2
            if media >= 6:
                status = "Aprovado!"
            else:
                status = "Reprovado!"

            aluno = {
                "nome": nome,
                "media": media,
                "status": status
            }

            alunos.append(aluno)
            print(aluno)
            print("Aluno Cadastrado!")
            
## // MENU
while True:
    menu()