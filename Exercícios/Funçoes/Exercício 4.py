#Classificar os triângulos por equilátero, isóceles ou escaleno
#Equilátero - todos os lados iguais
#Isóceles - dois lados com a mesma medida e um diferente
#Escaleno - todos os lados com medidas diferentes

def num():
    while True:
        try:
            num = float(input('Digite o valor do lado: '))
            return num
        except ValueError:
            print("Digite apenas números!")

def triangulo(num01, num02, num03):
    if num01 == num02 and num01 == num03 and num02 == num03:
        print("Esse triângulo é equilátero!")

    elif num01 == num02 or num01 == num03 or num02 == num03:
        print("Esse triângulo é isóceles!")

    elif num01 != num02 and num01 != num03 and num02 != num03:
        print("Esse triângulo é escaleno!")



num01 = num()
num02 = num()
num03 = num()

triangulo(num01, num02, num03)