def epar(n):
    if (n%1 == 1 or n%n == 1):
        print("V")
    else:
        print("F")

n = int(input("Digite o valor: "))
print(epar(n))








