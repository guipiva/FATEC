def menu():
    print('''
    Menu de Opções: 
    
    1 - Cadastrar 
    2 - Exibir Frase
    3 - Sair
    ''')
    opcao = int(input("Escolha uma opção: "))
    return(opcao)
while True:
    opcao = menu()

    if opcao == 1:
        print("vai corinthians")
    elif opcao == 2:
        print("avante timao")
    elif opcao == 3:
        break

print("Bye")

