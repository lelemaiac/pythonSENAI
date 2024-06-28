import random

numero_misterioso = random.randint(1, 100)

print("Jogo de adivinhação")
print("")
print("Olá, seja bem vindo ao jogo!")
print("Com esse jogo você irá ter a oportunidade de adivinhar o número misterioso!")
print("")


while True:
    try:
        numero_usuario = int(input("Digite um número de 1 a 100 para tentar acertar o misterioso: "))
        while numero_usuario < 1 or numero_usuario > 100:
            print("Tente novamente, digitando um número entre 1 e 100!")
            numero_usuario = int(input("Digite um número de 1 a 100 para tentar acertar o misterioso: "))
        break
    except ValueError:
        print("Dado inválido, tente novamente!")
if numero_usuario >= 1 and numero_usuario <= 100:
    while numero_usuario != 0:
        while True:

            if numero_usuario == numero_misterioso:
                print("Você acertou o número misterioso")
                print("")
                try:
                    novamente = input("Você gostaria de jogar novamente? (s/n) ")
                    if novamente == "s":
                        numero_misterioso = random.randint(1, 100)
                        print("")
                        numero_usuario = int(input("Digite um número de 1 a 100 para tentar acertar o misterioso: "))

                    elif novamente != "s":
                        print("Você saiu do jogo!")
                        numero_usuario = 0
                        break

                except ValueError:
                    print("Dado inválido, tente novamente!")

            while numero_usuario != numero_misterioso:
                if numero_usuario < numero_misterioso:
                    print("O número misterioso é maior que o número inserido, tente novamente!")

                elif numero_usuario > numero_misterioso:
                    print("O número misterioso é menor que o número escolhido, tente novamente!")
                numero_usuario = int(input("Digite um número de 1 a 100 para tentar acertar o misterioso: "))

else:
    print("Dados inválidos!")