def epar(n):
    if n%2 == 0:
        return True
    return False

x = int(input("Digite um valor: "))
if epar(x):
    print("O valor é par!")
else:
    print("o valor digitado é impar!")

    