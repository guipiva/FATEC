lista = []
for i in range(5):
    v = int(input(f"Digite 5 valores {i+1}: "))
    lista.append(v)

valor = max(lista)
print(max(lista), lista.index(valor))

