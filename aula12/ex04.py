from math import pi, pow
def area_circulo(raio):
    volume = ((4/3*pi) * raio**3)
    return volume

r = float(input("Digite o raio: "))
print(f"A area do circulo de raio {r} é igual a {area_circulo(r)}")

