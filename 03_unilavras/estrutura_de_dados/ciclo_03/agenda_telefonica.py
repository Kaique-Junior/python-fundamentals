contatos = {}

opcoes = {
    1: "Adicionar contato",
    2: "Buscar contato",
    3: "Listar contatos",
    4: "Sair"
}

def adicionar_contato():
    nome = input("\nNome do contato: ").strip()
    telefone = input("Telefone do contato: ").strip()
    
    if not nome:
        print("\nNome inválido. Operação cancelada.\n")
        return
        
    contatos[nome] = telefone
    print("\nContato adicionado!\n")

def buscar_contato():
    nome = input("\nNome do contato: ").strip()
    
    if nome in contatos:
        print(f"\nTelefone de {nome}: {contatos[nome]}\n")
    else:
        print("\nContato inexistente ou digitado incorretamente.\n")

def listar_contatos():
    if not contatos:
        print("\nA agenda está vazia.\n")
        return

    print("\n=== Lista de Contatos ===")
    for nome, telefone in contatos.items():
        print(f"{nome}: {telefone}")
    print()

def selecionar_opcao():
    fim = False
    
    while not fim:
        print("Seleciona uma das opções:")
        for num, opcao in opcoes.items():
            print(f"{num}: {opcao}")
            
        try:
            escolha = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("\nEntrada inválida! Digite apenas números.\n")
            continue
        
        match escolha:
            case 1:
                adicionar_contato()
            case 2:
                buscar_contato()
            case 3:
                listar_contatos()
            case 4:
                print("\nAgenda telefônica finalizada.")
                fim = True
            case _:
                print("\nOpção inválida, tente novamente!\n")

# Inicia a Agenda Telefônica
selecionar_opcao()