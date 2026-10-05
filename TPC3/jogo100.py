import random

jogar = "s"

while jogar == "s":

    print("\n=== CORRIDA PARA O 100 ===")
    print("1 - Computador joga primeiro")
    print("2 - Jogador joga primeiro")

    opcao = int(input("Escolha uma opção: "))

    while opcao != 1 and opcao != 2:
        print("Opção inválida!")
        opcao = int(input("Escolha 1 ou 2: "))

    total = 0

    # Computador joga primeiro
    if opcao == 1:

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
    jogar = input("\nQuer jogar novamente? (s/n): ").lower()

    while jogar != "s" and jogar != "n":
        print("Resposta inválida!")
        jogar = input("Quer jogar novamente? (s/n): ").lower()

print("\nObrigado por jogar!")