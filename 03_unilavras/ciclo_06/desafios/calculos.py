# Kaique Junior da Silva Oliveira

def calcular_area_triangulo(base, altura):
    return (base * altura) // 2

def calcular_volume_cubo(aresta):
    return aresta ** 3

base = int(input("Informe a base do triangulo: "))
altura = int(input("Informe a altura do triangulo: "))
aresta = int(input("Informe a aresta do cubo: "))

area_triangulo = calcular_area_triangulo(base, altura)
volume_cubo = calcular_volume_cubo(aresta)

print(f"\nÁrea do Triângulo: {area_triangulo}")
print(f"\nVolume do Cubo: {volume_cubo}")