import turtle

## Configuração básica
tela = turtle.Screen()
tela.setup(width=800, height=800, startx=1000, starty=0)
tela.title("Casa")
tela.bgcolor("black")

ninja = turtle.Turtle()
ninja.shape("turtle")
ninja.speed(5)
ninja.color("yellow")

# Funções

def teleport(x, y):
    ninja.teleport(x, y)

def position(prompt):
    pos = ninja.pos()
    print(f"{prompt}", pos)

def direita():
    ninja.setheading(180)

def frente(x):
    ninja.forward(x)

# Algoritmo para construir uma casa com o turtle

teleport(-200, -200)

for i in range(4):
    position("Posision quadrado:")
    ninja.forward(400)
    ninja.left(360 / 4)
    
ninja.teleport(200, 200)

ninja.teleport(0, 200)
ninja.setheading(90)
position("Posision 04:")
frente(200)
ninja.setheading(-45)
frente(282.84)

direita()
frente(400)



# Tem que estar sempre no final
tela.exitonclick()