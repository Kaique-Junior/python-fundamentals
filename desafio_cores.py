import turtle
import random

while True:
    n_lados = int(input("Digite o número de lados:"))

    if 3 <=  n_lados <= 30:
        break
    else:
        print("ERRO! É necessário escrever um número igual ou maior que 3 e menor que 31!")

tela = turtle.Screen()
tela.title("Poligono")
tela.bgcolor("black")

velocidade = 0 if n_lados >= 20 else 3

# Configuração do Ninja
cores = ["red", "blue", "green", "yellow", "purple"]

ninja = turtle.Turtle()
ninja.shape("turtle")
ninja.speed(velocidade)

# Movimentação do Ninja
tamanho_passo = 40 if n_lados >= 15 else 80

for i in range(n_lados):
    ninja.color(random.choice(cores))
    ninja.forward(tamanho_passo)
    ninja.left(360 / n_lados)

tela.exitonclick()