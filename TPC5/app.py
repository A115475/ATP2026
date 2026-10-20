def menu():
    print(""" 
    (1) Criar uma turma
    (2) Inserir um aluno na turma
    (3) Listar a turma
    (4) Consultar um aluno por id
    (8) Guardar a turma em ficheiro
    (9) Carregar uma turma dum ficheiro
    (0) Sair da aplicação
    """)

def criarTurma():
    print("Turma criada com sucesso (vazia).")
    return []

def lerNota(mensagem):
    # pedir a nota entre 0 e 20 + dar erro quando for diferente e pedir para repetir ate tar entre 0-20
    nota = float(input(mensagem))
    while nota < 0 or nota > 20:
        nota = float(input("Erro! Introduza uma nota válida (0 a 20): "))
    return nota

def existeID(id_procura, turma): # para em vez de ao dar um id repetido abrir de novo o menu, continuar ate dar um id diferente
    for aluno in turma:
        if aluno[1] == id_procura:
            return True
    return False

def inserirAluno(turma):
    nome = input("Nome do aluno: ")
    id_aluno = input("ID do aluno: ")
    
    # mensagem de erro
    while existeID(id_aluno, turma):
        print("Erro: Já existe um aluno com esse ID nesta turma!")
        id_aluno = input("Tente outra vez. Introduza um ID diferente: ")
            
    notaTPC = lerNota("Nota do TPC: ")
    notaProj = lerNota("Nota do Projeto: ")
    notaTeste = lerNota("Nota do Teste: ")
    
    aluno = (nome, id_aluno, [notaTPC, notaProj, notaTeste])
    turma.append(aluno)
    print("Aluno inserido!")
    return turma

def listarTurma(turma):
    if len(turma) == 0:
        print("A turma está vazia.")
    else:
        for aluno in turma:
            print(f"ID: {aluno[1]} | Nome: {aluno[0]} | Notas: {aluno[2]}")

def consultarAluno(turma):
    id_procura = input("Introduza o ID do aluno a procurar: ")
    encontrado = False
    for aluno in turma:
        if aluno[1] == id_procura:
            print(f"Encontrado - Nome: {aluno[0]} | Notas: {aluno[2]}")
            encontrado = True
    
    if encontrado == False:
        print("O ID não corresponde a nenhum aluno.")

def guardarTurma(turma):
    # verificar se a turma tem alunos antes de criar o ficheiro para nao dar erro por estar vazia
    if len(turma) == 0:
        print("Erro: A turma está vazia. Insira alunos primeiro antes de guardar!")
    else:
        nomefile = input("Indica o nome do ficheiro para guardar (ex: turma.txt): ")
        file = open(nomefile, "w")
        for aluno in turma:
            linha = f"{aluno[0]};{aluno[1]};{aluno[2][0]};{aluno[2][1]};{aluno[2][2]}\n"
            file.write(linha)
        file.close()
        print(f"Turma guardada em {nomefile}")

def carregarTurma():
    nomefile = input("Indica o nome do ficheiro a abrir (ex: turma.txt): ")
    turma = []
    file = open(nomefile, "r")
    for linha in file:
        campos = linha.strip().split(";")
        nome = campos[0]
        id_aluno = campos[1]
        notas = [float(campos[2]), float(campos[3]), float(campos[4])]
        aluno = (nome, id_aluno, notas)
        turma.append(aluno)
    file.close()
    print("Turma carregada com sucesso!")
    return turma

# menu
turma = []
opcao = "1"

while opcao != "0":
    menu()
    opcao = input("Introduza uma opção: ")
    
    if opcao == "1":
        turma = criarTurma()
    elif opcao == "2":
        turma = inserirAluno(turma)
    elif opcao == "3":
        listarTurma(turma)
    elif opcao == "4":
        consultarAluno(turma)
    elif opcao == "8":
        guardarTurma(turma)
    elif opcao == "9":
        turma = carregarTurma()
    elif opcao == "0":
        print("A terminar a aplicação. Até à próxima!")
    else:
        print("Opção inválida! Tente novamente.")