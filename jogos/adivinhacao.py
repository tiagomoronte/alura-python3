print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
chute = int(chute_str)

print("Você digitou ", chute)

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

print("Fim do jogo.")