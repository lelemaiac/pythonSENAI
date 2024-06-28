import random
numero_misterioso = random.randint(1, 100)


print("Jogo de adivinhação")
print("")
print("Olá, seja bem vindo ao jogo!")
print("")
print("Com esse jogo você irá ter a oportunidade de adivinhar o número misterioso!")
print("")

while True:
    try:
        numero_usuario = int(input("Digite um número de 1 a 100 para tentar acertar o mistérioso: "))
        break
    except ValueError:
        print("Dado inválido, tente novamente!")

    if numero_usuario >= 1 and numero_usuario <= 4:
        while numero_usuario != 0:
            while True:
                try:
                    if numero_usuario < numero_misterioso:
                        break
                except ValueError:
                    print("O número misterioso é maior que o número inserido")


            elif numero_usuario > numero_misterioso:

                except ValueError:
                    print("O número misterioso é menor que o número inserido")

                print("Jogo de adivinhação")
                print("")
                print("Olá, seja bem vindo ao jogo!")
                print("")
                print("Com esse jogo você irá ter a oportunidade de adivinhar o número misterioso!")
                print("")

            else:
            print("Dados inválidos")
