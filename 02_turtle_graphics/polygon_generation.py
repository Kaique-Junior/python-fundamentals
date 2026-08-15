import turtle
import random

# # Input de Lados
while True:
    try:
        n_lados = int(input("Digite o número de lados (De 3 a 30):"))
        if 3 <= n_lados <= 30:
            break
        else:
            print("ERRO! Você digitou um número fora do permitido!")
    except ValueError:
        print("ERRO! Digite apenas números inteiros, não letras ou símbolos!")

# Input de Passos
while True:
    try:
        tamanho_passo = int(input("Digite o tamanho do passo (De 10 a 60):"))
        if 10 <= tamanho_passo <= 60:
            break
        else:
            print("ERRO! Digite um número de 10 a 60 para rodar!")
    except ValueError:
        print("ERRO! Digite apenas números inteiros, não letras ou símbolos!")

# Input de Velocidade
while True:
    try:
        ninja_velocidade = int(input("Digite a velocidade (De 0 a 10)"))
        if 0 <= ninja_velocidade <= 10:
            break
        else:
            print("ERRO! Digite um número de 0 a 10 para rodar!")
    except ValueError:
            print("ERRO! Digite apenas números inteiros, não letras ou símbolos!")


move_confirm = input("Deseja mover a tartaruga para criar vários poligonos? (Y / N)")
if move_confirm == "Y" or move_confirm == "y":
    try:
        print("------------------------------------")
        print("Turtle sempre começa em x = 0, y = 0")
        print("------------------------------------")
        x1 = int(input("Digite o valor do x:"))
        y1 = int(input("Digite o valor do y:"))
    except:
        print("Coordenadas inválidas! O segundo polígono não será desenhado.")
        move_confirm = "N"
else:
    print("Certo!")

# Listas
cores = ["blue", "yellow", "purple", "pink", "red", "green"]

# Funções
def desenhar_poligono(t, lados, tamanho):
    for i in range(lados):
        t.color(random.choice(cores))
        t.forward(tamanho)
        t.left(360 / lados)

def mover_ninja(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Tela
tela = turtle.Screen()
tela.bgcolor("black")
tela.title("Gerador de Poligonos")

# Ninja
ninja = turtle.Turtle()
ninja.shape("turtle")
ninja.color("pink")
ninja.speed(ninja_velocidade)

# Movimentação
for i in range(2):
    desenhar_poligono(ninja, n_lados, tamanho_passo)
    if move_confirm == "Y" or move_confirm == "y":
        mover_ninja(ninja, x1, y1)
        desenhar_poligono(ninja, n_lados, tamanho_passo)

tela.exitonclick()