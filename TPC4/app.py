import random

def menu():
    print("############\n### MENU ###\n############\n# [1] Criar Lista\n# [2] Ler Lista\n# [3] Soma\n# [4] Média\n# [5] Maior\n# [6] Menor\n# [7] Está ordenada por ordem crescente\n# [8] Está ordenada por ordem decrescente\n# [9] Procura um elemento\n# [0] Sair")

def criarLista():
    N = int(input("Quantos números quer gerar? "))
    lista = []
    i = 0
    while i < N:
        lista.append(random.randint(1, 100))
        i = i + 1
    return lista

def lerLista():
    N = int(input("Quantos números quer introduzir? "))
    lista = []
    i = 0
    while i < N:
        num = int(input(f"Introduza o elemento {i+1}: "))
        lista.append(num)
        i = i + 1
    return lista

def somaLista(lista):
    res = 0
    for n in lista:
        res = res + n
    return res

def mediaLista(lista):
    res = somaLista(lista)
    return res / len(lista)

def maiorLista(lista):
    res = lista[0]
    for n in lista:
        if n > res:
            res = n
    return res

def menorLista(lista):
    res = lista[0]
    for n in lista:
        if n < res:
            res = n
    return res

def estaOrdenadaC(lista):
    i = 0
    while i < len(lista) - 1:
        if lista[i] > lista[i+1]:
            return "Não"
        i = i + 1
    return "Sim"

def estaOrdenadaD(lista):
    i = 0
    while i < len(lista) - 1:
        if lista[i] < lista[i+1]:
            return "Não"
        i = i + 1
    return "Sim"

def procuraElemento(lista, elem):
    i = 0
    while i < len(lista):
        if lista[i] == elem:
            return i  
        i = i + 1
    return -1  

listaInterna = []
opcao = -1

while opcao != 0:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        listaInterna = criarLista()
        print("Lista criada com sucesso:", listaInterna)
        
    elif opcao == 2:
        listaInterna = lerLista()
        print("Lista introduzida com sucesso:", listaInterna)
        
    elif opcao == 3:
        if len(listaInterna) > 0:
            print("Soma:", somaLista(listaInterna))
        else:
            print("Erro: A lista está vazia.")
            
    elif opcao == 4:
        if len(listaInterna) > 0:
            print("Média:", mediaLista(listaInterna))
        else:
            print("Erro: A lista está vazia.")
            
    elif opcao == 5:
        if len(listaInterna) > 0:
            print("Maior elemento:", maiorLista(listaInterna))
        else:
            print("Erro: A lista está vazia.")
            
    elif opcao == 6:
        if len(listaInterna) > 0:
            print("Menor elemento:", menorLista(listaInterna))
        else:
            print("Erro: A lista está vazia.")
            
    elif opcao == 7:
        if len(listaInterna) > 0:
            print("A lista está ordenada por ordem crescente?", estaOrdenadaC(listaInterna))
        else:
            print("Erro: A lista está vazia.")
            
    elif opcao == 8:
        if len(listaInterna) > 0:
            print("A lista está ordenada por ordem decrescente?", estaOrdenadaD(listaInterna))
        else:
            print("Erro: A lista está vazia.")
            
    elif opcao == 9:
        if len(listaInterna) > 0:
            elem = int(input("Que elemento quer procurar? "))
            pos = procuraElemento(listaInterna, elem)
            if pos != -1:
                print(f"Elemento encontrado na posição: {pos}")
            else:
                print("Elemento não encontrado (-1).")
        else:
            print("Erro: A lista está vazia.")
            
    elif opcao == 0:
        print("A finalizar o programa...")
        print("Lista final guardada:", listaInterna)
        
    else:
        print("Opção inválida! Tente novamente.")
