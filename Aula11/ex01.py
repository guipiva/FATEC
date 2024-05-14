lista = []
n = int

for i in range(10):
    n = int(input(f"Digite o {n}: "))
    lista.append(n)

t = tuple(lista)
print(t[::-1])


