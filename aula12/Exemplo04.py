from math import pow
def potencia(numero, expoente = 2):
    resultado = pow(numero, expoente)
    return resultado

n = float(input("Digite o numero: "))
e = int(input("Expoente: "))

print(f"Valor com expoente: {potencia(n,e)}")
print(f"valor sem o expoente: {potencia(n)}")

