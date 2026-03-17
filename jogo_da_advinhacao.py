import random

def jogar():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    limite = 7

    print("Tente adivinhar o número entre 1 e 100")

    while tentativas < limite:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite == numero_secreto:
            print("Você acertou em", tentativas, "tentativas!")
            return
        elif palpite < numero_secreto:
            print("O número é maior")
        else:
            print("O número é menor")

        print("Tentativas restantes:", limite - tentativas)

    print("Você perdeu! O número era", numero_secreto)

def main():
    while True:
        jogar()
        jogar_novamente = input("Quer jogar de novo? (s/n): ").lower()
        if jogar_novamente != "s":
            break

main()
