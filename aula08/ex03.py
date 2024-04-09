frase = str(input("Digite uma frase: "))
v = 0

for letra in frase:
    if letra.upper() in "AEIOU":
        v = v + 1

print(f"A frase tem {v} vogals(is)")





