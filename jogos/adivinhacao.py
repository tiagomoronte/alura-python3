print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 42
total_de_tentativas = 3
acertou = False

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

    rodada += 1

print("Fim do jogo.")
