import random

def jogar():

    print("Bem vindo ao jogo de adivinhação")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) facil (2) medio (3) dificil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"rodada {rodada} de {total_de_tentativas}")
        chute = int(input("digite o seu número: "))

        print("voce digitou: ", chute)
        if (chute < 1 or chute > 100):
            print("voce deve digitar um valor entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = numero_secreto < chute

        if (acertou):
            print(f"voce acertou! Fez {pontos}")
            break
        elif (maior):
            print("voce errou para cima!")
        else:
            print("voce errou para baixo!")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    print("fim do jogo")

if (__name__ == "__main__"):
    jogar()