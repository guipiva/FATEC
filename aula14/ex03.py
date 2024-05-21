numero =input("Digite um numero positivo: ")
tupla1 = tuple(numero)
tupla2 = tuple(map(int, tupla1))

soma = sum(tupla2)
mult = 1

for i in tupla2:
    mult = mult * i

print(f"O valor da multiplicaçao de todos digitos e igual a :{mult}")
print(f"O valor da soma de todos os digitos e igual a:{soma}")

