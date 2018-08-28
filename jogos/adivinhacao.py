import random

print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = int(random.randrange(1, 101)) # entre 0.0 e 1.0
total_de_tentativas = 0
pontos = 1000

print("Qual o níevel de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))
if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    print("Voce digitou ", chute)

    if (chute < 1 or chute > 100):
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Parabens")
        break
    else:
        if (maior):
            print("Chute maior")
        elif (menor):
            print("Chute menor")
        pontos = pontos - (abs(numero_secreto - chute))

    rodada += 1

print("Pontos {}".format(pontos))
print (numero_secreto)
print("Fim do jogo.")
