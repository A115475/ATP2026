print("Olá! Pensa num número entre 1 e 100." "\nAs únicas respostas validas são 'maior', 'menor' ou 'certo'.")

inferior = 1
superior = 100

while inferior <= superior:
    tentativa = (inferior + superior)// 2
    print("hmmm deixa me pensar...")

    resposta = input("O teu número é " + str(tentativa) + "? ")

    if resposta == "certo":
        print("Acertei!")
        break

    elif resposta == "maior":
        inferior = tentativa + 1

    elif resposta == "menor":
        superior = tentativa - 1

    else:
        print("As únicas respostas validas são 'maior', 'menor' ou 'certo' como mencionado no inicio do jogo!")
