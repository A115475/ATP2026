
import random


lista = []
opcao = -1

while opcao != 0:
    print("############\n### MENU ###\n############\n# [1] Criar Lista\n# [2] Ler Lista\n# [3] Soma\n# [4] Média\n# [5] Maior\n# [6] Menor\n# [7] Está ordenada por ordem crescente\n# [8] Está ordenada por ordem decrescente\n# [9] Procura um elemento\n# [0] Sair")

    opcao = int(input("Escolhe uma opção: "))

    if opcao == 1:
        def criar_lista_aleatoria():
            n = int(input("Quantos números queres gerar? "))
            lista = []

            for i in range(n):
                lista.append(random.randint(1, 100))

            return lista

        lista = criar_lista_aleatoria()
        print("Lista criada:", lista)

    elif opcao == 2:
        def ler_lista():
            n = int(input("Quantos números queres introduzir? "))
            lista = []

            for i in range(n):
                numero = int(input(f"Introduz o número {i + 1}: "))
                lista.append(numero)

            return lista

        lista = ler_lista()
        print("Lista introduzida:", lista)

    elif opcao == 3:
        def soma(lista):
            resultado = 0

            for i in range(len(lista)):
                resultado = resultado + lista[i]

            return resultado

        if len(lista) > 0:
            print("Soma:", soma(lista))
        else:
            print("A lista está vazia.")

    elif opcao == 4:
        def media(lista):
            resultado = 0

            for i in range(len(lista)):
                resultado = resultado + lista[i]

            return resultado / len(lista)

        if len(lista) > 0:
            print("Média:", media(lista))
        else:
            print("A lista está vazia.")

    elif opcao == 5:
        def maior(lista):
            resultado = lista[0]

            for i in range(1, len(lista)):
                if lista[i] > resultado:
                    resultado = lista[i]

            return resultado

        if len(lista) > 0:
            print("Maior elemento:", maior(lista))
        else:
            print("A lista está vazia.")

    elif opcao == 6:
        def menor(lista):
            resultado = lista[0]

            for i in range(1, len(lista)):
                if lista[i] < resultado:
                    resultado = lista[i]

            return resultado

        if len(lista) > 0:
            print("Menor elemento:", menor(lista))
        else:
            print("A lista está vazia.")

    elif opcao == 7:
        def esta_ordenada_crescente(lista):
            for i in range(len(lista) - 1):
                if lista[i] > lista[i + 1]:
                    return "Não"

            return "Sim"

        print("Ordenada por ordem crescente:",
              esta_ordenada_crescente(lista))

    elif opcao == 8:
        def esta_ordenada_decrescente(lista):
            for i in range(len(lista) - 1):
                if lista[i] < lista[i + 1]:
                    return "Não"

            return "Sim"

        print("Ordenada por ordem decrescente:",
              esta_ordenada_decrescente(lista))

    elif opcao == 9:
        def procura_elemento(lista, elemento):
            for i in range(len(lista)):
                if lista[i] == elemento:
                    return i

            return -1

        elemento = int(input("Que elemento quer procurar? "))
        print("Posição:", procura_elemento(lista, elemento))

    elif opcao == 0:
        print("A finalizar o programa...")
        print("Lista final:", lista)

    else:
        print("Opção inválida!")

print("Programa terminado.")