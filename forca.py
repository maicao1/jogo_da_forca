def jogar_forca():
    print("-------------------------------")
    print("\nBem vindo ao jogo da forca!\n")
    print("-------------------------------")

    palavra_secreta = "processador".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    perdeu = False
    acertou = False
    erros = 0

    arquivo = open ("jogos/palavras.txt", "r")
    palavras = []

    for linha in palavras:
        linha = linha.strip()
        palavras.append(linha)
        

    while (not perdeu and not acertou):
        chute = input("Escreva uma letra: ")
        chute = chute.strip().upper()

        #index define a posição da letra
        index = 0
        if (chute in palavra_secreta ):
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
         
        else: 
         erros = erros + 1
        
         perdeu = erros == 6

        acertou = "_" not in letras_acertadas
         

        print(letras_acertadas)
if(__name__ == "__main__"):
    jogar_forca()


