maior_imc = 0
menor_imc = 100
soma_altura = 0
soma_peso = 0
for k in range (1,6):
    peso = float(input("Digite seu peso: (em kg)"))
    altura = float(input("Digite sua altura: "))
    imc = peso / (altura * altura)
pesom= peso / 5
alturam= altura / 5
print(pesom)
print(alturam)
print(imc>24)
print(imc<24)