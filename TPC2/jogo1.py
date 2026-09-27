import random

numero = random.randint(1, 100)

print("Pensei num número entre 1 e 100, tenta adivinhar qual é!")

while True:
    tentativa = int(input("Diz um número: "))

    if tentativa < numero:
        print("É maior, tenta outra vez!")
    elif tentativa > numero:
        print("É menor, tenta outra vez!")
    else:
        print("Acertaste em cheio!")
        break