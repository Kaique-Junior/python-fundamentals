# Desafio 3

niveis = {
    1: 12,
    2: 17,
    3: 25,
}

while True:
    try: # Uso do Try e Except para tratamento de erro

        print("\n--- Tabela de Níveis de Professor ---")

        for nv, dinheiro in niveis.items(): # Pega todos os items do dicionário
            print(f"Professor [Nível: {nv}] | R${dinheiro:.2f} por hora/aula")

        nivel = int(input("\nInforme o nível desse professor: "))

        if nivel not in niveis.keys(): # Pega todas as chaves do dicionário
            print("\nERRO! O número digitado não é válido!\n")
            continue

        horas_aulas = float(input("Informe quantas horas/aulas o professor deu: "))
        break # Interrompe o Loop Principal
    
    except ValueError:
        print("\nERRO! Digite apenas números inteiros.\n")
        continue

salario = niveis[nivel] * horas_aulas
print(f"Seu salário é de R${salario:.2f}")
