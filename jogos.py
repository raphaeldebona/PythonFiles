import forca
import adivinhacao

print("Bem vindo, escolha o seu jogo")
jogo = 0

while True:
    print("(1) adivinhação (2) forca")
    jogo = int(input("Qual jogo?\n"))
    if(jogo == 1):
        print("jogando adivinhacao")
        adivinhacao.jogar()
        break
    elif(jogo == 2):
        print("jogando forca")
        forca.jogar()
        break
    else:
        print("entrada invalida, favor inserir 1 ou 2")