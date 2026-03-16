
def jogar_forca():

    print('*--------------------*')
    print('BEM VINDO AO JOGO DE FORCA')
    print('*--------------------*')

    palavra_secreta = "carambola"
    perdeu = False
    acertou = False

    while(not perdeu and not acertou):
        chute = input('Digite uma Letra: ')
        chute.strip()
        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
             print(f"A letra {chute} esta na posição {index}")
             index = index + 1























if(__name__ == "__main__"):
    jogar_forca()