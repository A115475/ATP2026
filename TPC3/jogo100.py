import random

jogar = "sim"

while jogar == "sim":

    print("\nBem vindo ao jogo CORRIDA PARA O 100!\nEscolha o modo de jogo:")
    print("computador - O computador joga primeiro")
    print("eu - Você joga primeiro")

    opcao = input("Escolha uma opção: ").lower()

    while opcao != "computador" and opcao != "eu":
        print("Opção inválida!")
        opcao = input("Escolha computador ou eu: ").lower()

    total = 0

    # Computador joga primeiro
    if opcao == "computador":

        while total < 100:

            if total == 0:
                jogada = 1
            else:
                jogada = 10 - (total % 10)

            total = total + jogada

            print("Computador jogou:", jogada)
            print("Total:", total)

            if total == 100:
                print("O computador ganhou!")
                break

            jogada = int(input("Escolha um número de 1 a 10: "))

            while jogada < 1 or jogada > 10:
                print("Jogada inválida!")
                jogada = int(input("Escolha um número de 1 a 10: "))

            total = total + jogada

            print("Total:", total)

            if total == 100:
                print("O jogador ganhou!")

    # Jogador joga primeiro
    else:

        while total < 100:

            jogada = int(input("Escolha um número de 1 a 10: "))

            while jogada < 1 or jogada > 10:
                print("Jogada inválida!")
                jogada = int(input("Escolha um número de 1 a 10: "))

            total = total + jogada

            print("Total:", total)

            if total == 100:
                print("O jogador ganhou!")
                break

            jogada = 10 - (total % 10)

            if jogada == 10:
                jogada = random.randint(1, 10)

            total = total + jogada

            print("Computador jogou:", jogada)
            print("Total:", total)

            if total == 100:
                print("O computador ganhou!")

    # Perguntar se quer jogar novamente
    jogar = input("\nQuer jogar novamente?\nRespostas válidas:sim/nao ").lower()

    while jogar != "sim" and jogar != "nao":
        print("Resposta inválida!")
        jogar = input("Quer jogar novamente?\nRespostas válidas:sim/nao ").lower()

print("\nObrigado por jogar!")