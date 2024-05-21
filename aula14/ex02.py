valor = int(input("Digite o valor(RA):"))
primos = []
soma = 0
calculo = valor * 2 + 5

for numero in range(calculo + 1):
    if numero < 2:
        continue
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    if primo:
        primos.append(numero)
        soma += numero

print(f"A lista de numeros primos ate {calculo}:{primos}")
print(f"A soma dos numeros primos e de:{soma}")

