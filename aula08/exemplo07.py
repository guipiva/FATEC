nome = input("Digite seu nome completo: ")
nascimento = input("Digite sua data de nascimento:<DD/MM/AAAA>")
data = nascimento.split('/')
palavras = nome.split()
pre_nome = palavras[0]
sobrenome = palavras[1]

print(f"Olá {pre_nome},... Muito bonito seu sobrenome {sobrenome}")
print(f"Voce nasceu no dia {data[0]} e no mês {data[1]}")
