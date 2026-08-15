import turtle

## Configuração Tela
tela = turtle.Screen()
tela.setup(width=800, height=800, startx=1000, starty=0)
tela.title("Casa")
tela.bgcolor("darkblue")

## Configuração Turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(5)
t.pensize(5)

# Funções

# Importante para calcular onde preciso teleportar a turtle
def position(t, prompt):
    print(f"{prompt}:", t.pos())

# Para encontrar o tamanho da hipotenusa para o telhado
def hypotenuse(a, b):
    return (a**2 + b**2) ** (1/2)

## FLUXO PARA FAZER UMA CASA

## Quadrado da Casa
t.begin_fill()
t.teleport(-200,-200)
t.color("navajo white")

for i in range(4):
    t.forward(400)
    t.left(360 / 4)

## Telhado
t.teleport(-200, 200)
t.setheading(45)
t.color("light coral")

for i in range(2):
    t.forward(hypotenuse(200, 200))
    t.right(90)

## Porta
t.teleport(-100, -200)
t.color("saddle brown")

t.setheading(90)
t.forward(200)
t.setheading(0)
t.forward(100)
t.setheading(270)
t.forward(200)

# Porta - Maçaneta
t.teleport(-30, -100)
t.color("black")
t.pensize(2)

t.circle(5)

t.end_fill()
t.hideturtle()

#/
tela.exitonclick()