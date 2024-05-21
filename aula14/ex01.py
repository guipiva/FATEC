numero_cabecas = int(input("Digite a quantidade de cabeças: "))
numero_patas = int(input("Digite a quantidade de patas: "))

if (numero_cabecas < numero_patas):
    coelhos = int((numero_patas - 2 * numero_cabecas) / 2)
    patos = int(numero_cabecas - coelhos)

    print(f"Coelhos: {str(coelhos)}")
    print(f"Patos: {str(patos)}")
elif (numero_patas == numero_cabecas):
    print("Numero invalido")
else:
    print("Numero invalido")

