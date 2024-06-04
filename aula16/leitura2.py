with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())

print("FIM!")
