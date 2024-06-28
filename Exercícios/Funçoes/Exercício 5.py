print("Calculadora de IMC")

def peso():
    while True:
        try:
            peso = float(input("Digite seu peso em KG: "))
            return peso
        except ValueError:
            print("Digite apenas números e caso seja decimal, utilize ponto. Ex: 55.8")
def altura():
    while True:
        try:
            altura = float(input("Digite sua altura em Metros: "))
            if altura >= 1 and altura <= 2.5:
                return altura
            else:
                print("Dado inválido, tente de 1 a 2.5!")

        except ValueError:
            print("Digite apenas números!")


def calculo(peso, altura):
    imc = peso / (altura * altura)
    return imc


def resultado(imc):
    if imc >= 17 and imc <= 18.4:
        print("Seu IMC está ma cateqoria abaixo do peso!")
    elif imc >= 18.6 and imc <= 24.9:
        print("Seu IMC está na categoria peso normal!")
    elif imc >= 25 and imc <= 29.9:
        print("Seu IMC está na categoria sobrepesso!")
    elif imc >= 30 and imc <= 40:
        print("Seu IMC está na categoria obesidade!")
    else:
        print("erro, imc:", imc)


resultado_imc = calculo(peso(), altura())

resultado(resultado_imc)
