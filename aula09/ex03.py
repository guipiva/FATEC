lista = []
lista2 = []

for i in range(5):
    v = int(input(f"Digite 5 valores {i+1}: "))
    lista.append(v)

for i in range(5):
    v2 = int(input(f"Digite 5 valores {i+1}: "))
    lista.append(v2)

print(lista + lista2)

