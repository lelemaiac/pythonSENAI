def menu():
    print("Bem vindo a calculadora!")
    print("1- Adição")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")
    print("5- Todas")


def opcao():
    while True:
        try:
            escolha = int(input("Digite o que você deseja, entre 1 e 5: "))
            if escolha >= 1 and escolha <= 5:
                return escolha
            else:
                print("Dado inválido, digite um número de 1 a 5!")
        except ValueError:
            print("Digite apenas números inteiros, como 1, 2, 3, 4, 5")


def num():
    while True:
        try:
            num = float(input("Digite o número: "))
            return num
        except ValueError:
            print("Digite apenas números e caso seja decimal, utilize ponto. Ex: 2.5")


def soma(num01, num02):
    soma = num01 + num02
    return soma

def subtracao(num01, num02):
    subtracao = num01 - num02
    return subtracao
def multiplicacao(num01, num02):
    multiplicacao = num01 * num02
    return multiplicacao
def divisao(num01, num02):
    divisao = num01 / num02
    return divisao

def todas(num01, num02):
    print("Sua soma deu:", soma(num01, num02))
    print("Sua subtração deu:", subtracao(num01, num02))
    print("Sua multiplicação deu:", multiplicacao(num01, num02))
    print("Sua divisâo deu:", divisao(num01, num02))

menu()
option = opcao()
num01 = num()
num02 = num()
calculos = (soma, subtracao, multiplicacao, divisao)

if option == 1:
    print("Sua soma deu:", soma(num01, num02))
elif option == 2:
    print("Sua subtração deu:", subtracao(num01, num02))
elif option == 3:
    print("Sua multiplicação deu:", multiplicacao(num01, num02))
elif option == 4:
    print("Sua divisâo deu:", divisao(num01, num02))
elif option == 5:
    todas(num01, num02)