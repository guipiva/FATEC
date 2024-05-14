from math import pi, pow
def area_circulo(raio):
    area = pi * pow(raio, 2)
    return area

r = float(input("Digite o raio: "))
print(f"A area do circulo de raio {r} é igual a {area_circulo(r)}")

