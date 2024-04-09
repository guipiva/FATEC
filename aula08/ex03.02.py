frase = str(input("Digite uma frase: "))
v = 0

for vogal in "AEIOUaeiou":
        v = v + frase.count(vogal)

print(f"A frase tem {v} vogals(is)")


