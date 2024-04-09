data = str(input("Digite uma data <dd/mm/aaaa>"))
separa = data.split('/')

print(f"{separa[2]}/{separa[1]}/{separa[0]}")