largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
comprimento = float(input("Digite o comprimento: "))
metros = (largura * altura * comprimento - 16.8)
tinta = (metros / 3)
latas = (tinta / 3.7)

print("voce vai precisar de: {:.3} de tinta de 3,7 litros".format(latas))
print(metros)

