# Nome: Kaique Junior da Silva Oliveira
# Exercício 3 - Akinator Simplificado

def pergunta(prompt):
    while True:
        try:
            resposta = int(input(f"{prompt}: "))

            if resposta not in [1, 2]:
                print("ERRO! Digite apenas 1 para SIM ou 2 para NÃO")
                continue
            else:
                return resposta
        except ValueError:
            print("ERRO! Digite apenas (1) para SIM ou (2) para NÃO")
            continue

animais = ("Leão", "Águia", "Jacaré", "Tubarão", "Sapo")

print("--- Akinator Simplificado ---\n")
print("Pense em um dos animais da lista:")
for animal in animais:
    print(f"• {animal}")

print("\nDigite (1) para SIM ou (2) para NÃO\n")

vive_agua = pergunta("Vive na água?")

if vive_agua == 1:
    patas = pergunta("O animal tem quatro patas?")
    if patas == 1:
        grande = pergunta("O animal é considerado grande?")
        if grande == 1:
            print("\nSeu animal é o JACARÉ!")
        else:
            print("\nSeu animal é o SAPO!")
    else:
        print("\nSeu animal é o TUBARÃO!")
else:
    voa = pergunta("O animal sabe voar?")
    if voa == 1:
        print("\nSeu animal é a ÁGUIA!")
    else:
        print("\nSeu animal é o LEÃO!")