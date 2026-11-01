import matplotlib.pyplot as plt

def menu():
    print("""
    --- Tabela Meteorológica ---
    (1) Calcular temperaturas médias
    (2) Guardar tabela em ficheiro
    (3) Carregar tabela de ficheiro
    (4) Calcular temperatura mínima mais baixa
    (5) Calcular amplitude térmica
    (6) Calcular dia de precipitação máxima
    (7) Listar dias com precipitação superior a p
    (8) Maior período de dias com precipitação abaixo de p
    (9) Desenhar gráficos (Min, Max, Pluviosidade)
    (0) Sair
    """)

def medias(tabela):
    res = []
    for reg in tabela:
        data = reg[0]
        tmin = reg[1]
        tmax = reg[2]
        media = (tmin + tmax) / 2
        res.append((data, media))
    return res

def guardatabela(t, nomef):
    f = open(nomef, "w")
    for reg in t:
        data = reg[0]
        tmin = reg[1]
        tmax = reg[2]
        precip = reg[3]
        # para guardar data separada e os outros valores
        linha = f"{data[0]};{data[1]};{data[2]};{tmin};{tmax};{precip}\n"
        f.write(linha)
    f.close()
    print(f"Tabela guardada no ficheiro {nomef}.")

def carregatabela(nomef):
    res = []
    f = open(nomef, "r")
    for linha in f:
        campos = linha.strip().split(";")
        data = (int(campos[0]), int(campos[1]), int(campos[2]))
        tmin = float(campos[3])
        tmax = float(campos[4])
        precip = float(campos[5])
        res.append((data, tmin, tmax, precip))
    f.close()
    print("Tabela carregada com sucesso.")
    return res

def minMin(tabela):
    minima = tabela[0][1]
    for reg in tabela:
        if reg[1] < minima:
            minima = reg[1]
    return minima

def amplTerm(tabela):
    res = []
    for reg in tabela:
        data = reg[0]
        amp = reg[2] - reg[1]
        res.append((data, amp))
    return res

def maxChuva(tabela):
    max_data = tabela[0][0]
    max_prec = tabela[0][3]
    for reg in tabela:
        if reg[3] > max_prec:
            max_prec = reg[3]
            max_data = reg[0]
    return (max_data, max_prec)

def diasChuvosos(tabela, p):
    res = []
    for reg in tabela:
        if reg[3] > p:
            res.append((reg[0], reg[3]))
    return res

def maxPeriodoCalor(tabela, p):
    max_consec = 0
    atual_consec = 0
    for reg in tabela:
        if reg[3] < p:
            atual_consec = atual_consec + 1
            if atual_consec > max_consec:
                max_consec = atual_consec
        else:
            atual_consec = 0
    return max_consec

def graftabela(t):
    datas = []
    tmins = []
    tmaxs = []
    precips = []
    
    for reg in t:
        data_str = f"{reg[0][0]}/{reg[0][1]}/{reg[0][2]}"
        datas.append(data_str)
        tmins.append(reg[1])
        tmaxs.append(reg[2])
        precips.append(reg[3])
        
    plt.plot(datas, tmins, label="Temp Min", color="blue", marker="o")
    plt.plot(datas, tmaxs, label="Temp Max", color="red", marker="o")
    plt.plot(datas, precips, label="Pluviosidade", color="green", marker="o")
    
    plt.xlabel("Datas")
    plt.ylabel("Valores")
    plt.title("Evolução Meteorológica")
    plt.legend()
    plt.show()

# menu
tabelaMeteo = [((2022,1,20), 2, 16, 0), ((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]
opcao = "1"

while opcao != "0":
    menu()
    opcao = input("Introduza uma opção: ")
    
    if opcao == "1":
        if len(tabelaMeteo) > 0:
            print("Médias de cada dia:", medias(tabelaMeteo))
        else:
            print("Erro: Tabela vazia.")
            
    elif opcao == "2":
        if len(tabelaMeteo) > 0:
            nomef = input("Nome do ficheiro para guardar (ex: meteo.txt): ")
            guardatabela(tabelaMeteo, nomef)
        else:
            print("Erro: Tabela vazia.")
            
    elif opcao == "3":
        nomef = input("Nome do ficheiro para carregar (ex: meteo.txt): ")
        tabelaMeteo = carregatabela(nomef)
        
    elif opcao == "4":
        if len(tabelaMeteo) > 0:
            print("Temperatura mínima mais baixa:", minMin(tabelaMeteo))
        else:
            print("Erro: Tabela vazia.")
            
    elif opcao == "5":
        if len(tabelaMeteo) > 0:
            print("Amplitude térmica de cada dia:", amplTerm(tabelaMeteo))
        else:
            print("Erro: Tabela vazia.")
            
    elif opcao == "6":
        if len(tabelaMeteo) > 0:
            resultado = maxChuva(tabelaMeteo)
            print(f"Precipitação máxima foi no dia {resultado[0]} com valor {resultado[1]}")
        else:
            print("Erro: Tabela vazia.")
            
    elif opcao == "7":
        if len(tabelaMeteo) > 0:
            p = float(input("Introduza o limite p de precipitação: "))
            print(f"Dias com precipitação > {p}:", diasChuvosos(tabelaMeteo, p))
        else:
            print("Erro: Tabela vazia.")
            
    elif opcao == "8":
        if len(tabelaMeteo) > 0:
            p = float(input("Introduza o limite p de precipitação: "))
            print(f"Maior período de dias com precipitação < {p}: {maxPeriodoCalor(tabelaMeteo, p)} dias consecutivos.")
        else:
            print("Erro: Tabela vazia.")
            
    elif opcao == "9":
        if len(tabelaMeteo) > 0:
            graftabela(tabelaMeteo)
        else:
            print("Erro: Tabela vazia.")
            
    elif opcao == "0":
        print("A sair da aplicação. Até à proxima!")
    else:
        print("Opção inválida! Tente novamente.")