arquivo=open("usuarios.txt", "r", encoding="utf-8")
for linha in arquivo:
    print(linha.strip())
arquivo.close()

