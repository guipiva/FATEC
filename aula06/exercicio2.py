compra = float(input("Digite o valor da sua compra: "))

if 1000 >= compra:
    print("Sua compra teve desconto, agora o valor é: ",compra - (compra * 0.1))
elif 1001 <= compra <= 5000:
    print("Sua compra teve desconto, agora o valor é: ",compra - (compra * 0.2))
else:
    print("Sua compra teve desconto, agora o valor é: ",compra - (compra * 0.3))