import turtle

# TELA
tela = turtle.Screen()
tela.title("Primeiro Algoritmo em Python com Turtle")
tela.bgcolor("black")

#
ninja = turtle.Turtle()
ninja.shape("turtle")
ninja.color("yellow")
ninja.speed(3)

for i in range(3):
    ninja.forward(180)
    ninja.left(360 / 3)

tela.exitonclick()