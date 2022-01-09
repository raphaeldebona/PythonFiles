import random


def jogar():

    mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()


    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print("\nVOCE GANHOU!!\n")
    else:
        print("\nVOCE PERDEU :(\n")

def mensagem_abertura():

    print("Bem vindo ao jogo de forca")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("qual letra?\n")
    chute = chute.strip().upper()
    return chute

def chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1


if (__name__ == "__main__"):
    jogar()