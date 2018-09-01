import random

print("###############################################")
print("###     BEM VINDO!!!! VAMOS JOGAR!!!!     #####")
print("###############################################")

numero1 = random.randrange(1,100)
numero2 = random.randrange(1,10)
resultado = numero1 * numero2

tentativa = int(input("Quanto é {} / {} ? ".format(resultado, numero1)))


if tentativa == numero2:
    print("Parabéns!!!")
else:
    print("Que pena... tente novamente! Beijo, me liga!!!! Fofa!!!")

