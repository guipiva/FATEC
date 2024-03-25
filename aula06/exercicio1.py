valor = int(input("Digite um valor: "))

if (valor / 3 %2) and (valor / 5 %2):
    print("esse valor é divisivel por 3 e 5", (valor / 3), (valor /5))
else:
    print("Esse valor não é divisivel por 3 e 5")
