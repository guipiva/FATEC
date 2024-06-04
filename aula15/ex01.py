jogo = str(input("Digite oque deseja jogar: "))

from random import choice
escolha = ["pedra", "papel", "tesoura"]
maq = choice(escolha)

if jogo == "pedra" and maq == "pedra":
    print(maq)
    print("Empate")
elif jogo == "pedra" and maq == "tesoura":
    print(maq)
    print("Voce ganhou")
elif jogo == "pedra" and maq == "papel":
    print(maq)
    print("Voce perdeu")
elif jogo == "papel" and maq == "papel":
    print(maq)
    print("Empate")
elif jogo == "papel" and maq == "tesoura":
    print(maq)
    print("Voce perdeu")
elif jogo == "papel" and maq == "pedra":
    print(maq)
    print("Voce ganhou")
elif jogo == "tesoura" and maq == "tesoura":
    print(maq)
    print("Empatou")
elif jogo == "tesoura" and maq == "papel":
    print(maq)
    print("Voce ganhou")
elif jogo == "tesoura" and maq == "pedra":
    print(maq)
    print("voce perdeu")
else:
    print("opcao invalida")


