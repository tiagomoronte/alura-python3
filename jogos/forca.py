
def jogar():

    print("*********************************")
    print("** Bem vindo ao jogo de forca! **")
    print("*********************************")

    palavra_secreta = "python"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Qual letra?").strip()

        index = 0
        for letra in palavra_secreta:
            if (letra.upper() == chute.upper()):
                print("Enconntrei a letra {} na posição {}".format(chute, index))
            index += 1

    print("Fim do jogo.")

if(__name__ =="__main__"):
    jogar()