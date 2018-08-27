print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")
chute = int(chute_str)

print("Você digitou ", chute)

if (numero_secreto == chute):
    print("Parabens")
else:
    print("Você errou")
