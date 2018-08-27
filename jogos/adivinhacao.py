print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1
acertou = False

while(rodada <= total_de_tentativas and not acertou):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ")
    chute = int(chute_str)

    print("Voce digitou ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Parabens")
    else:
        if (maior):
            print("Chute maior")
        elif (menor):
            print("Chute menor")

    rodada += 1

print("Fim do jogo.")