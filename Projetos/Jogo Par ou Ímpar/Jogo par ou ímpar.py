import random
numero_aleatorio = random.randint(1, 5)

print("Olá, seja bem vindo ao Jogo Par ou Ímpar!")
print("Para começarmos o jogo você deve escolher se quer par ou ímpar, vamos lá!")
print("")


while True:
    try:
        escolha = input("Digite se você gostaria de ser par ou impar: ")
        if escolha == "par" or escolha == "impar":
            numero_usuario = int(input("Digite um número entre 1 e 5: "))
            break
    except ValueError:
        print("Dado inválido, tente novamente!")

if numero_usuario >= 1 and numero_usuario <= 5:
    while numero_usuario != 0:
        while True:
            soma = numero_usuario + numero_aleatorio
            par_impar = soma % 2

            if escolha == "par":
                if par_impar == 0:
                    print("Você ganhou o jogo, pois a soma deu", soma, "ou seja deu par!")
                else:
                    print("Você perdeu, pois a soma deu", soma, "ou seja, deu ímpar, tente novamente!")

            elif escolha == "impar":
                if par_impar != 0:
                    print("Você ganhou o jogo, pois a soma deu", soma, "ou seja deu ímpar!")
                else:
                    print("Você perdeu, pois a soma deu", soma, "ou seja, deu par, tente novamente!")

            repetir = input("Deseja jogar novamente? (s/n)")

            print("")

            if repetir == "s" and numero_usuario >= 1 and numero_usuario <= 5:
                numero_aleatorio = random.randint(1, 5)
                while True:
                    try:
                        escolha = input("Digite se você gostaria de ser par ou impar: ")
                    except ValueError:
                        print("Dado inválido, tente novamente!")

                numero_usuario = int(input("Digite um número entre 1 e 5: "))
            else:
                print("Você saiu do jogo!")
                numero_usuario = 0
                break


else:
    print("Dados inseridos estão incorretos!")


