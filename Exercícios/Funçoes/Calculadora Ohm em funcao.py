def menu_inicial():
    print("Olá, seja bem-vindo a Calculadora Ohm.")
    print("Escolha qual você gostaria de calcular")
    print("1 - Resistência elétrica")
    print("2- Corrente elétrica")
    print("3- Tensão")
    print("4- Resistência do resistor")
    print("5- Sair")
    print("")

def menu():
    print("")
    print("Escolha qual você gostaria de calcular")
    print(" 1- Resistência elétrica \n 2- Corrente elétrica \n 3- Tensão \n 4- Resistência do resistor \n 5- Sair")
    print("")
def escolha():
    while True:
        try:
            escolha = int(input("Digite o que você deseja calcular: "))
            if escolha >= 1 and escolha <= 5:
                return escolha
            else:
                print("Digite apenas números de 1 a 4, sendo inteiro, exemplo: 1")

        except ValueError:
            print("Digite apenas números de 1 a 4, sendo inteiro, exemplo: 1")
def resistencia():
    while True:
        try:
            resistencia = float(input("Digite o valor da resistência em ohms: "))
            if resistencia != 0:
                return resistencia
        except ValueError:
            print("Digite apenas números e caso seja decimal utilize ponto, exemplo: 5.5")

def corrente():
    while True:
        try:
            corrente = float(input("Digite o valor da corrente em ampere: "))
            if corrente != 0:
                return corrente
        except ValueError:
            print("Digite apenas números e caso seja decimal utilize ponto, exemplo: 5.5")

def tensao():
    while True:
        try:
            tensao = float(input("Digite o valor da tensão em volts: "))
            if tensao != 0:
                return tensao
        except ValueError:
            print("Digite apenas números e caso seja decimal utilize ponto, exemplo: 8.5")

def tensao_fonte():
    while True:
        try:
            tensao_fonte = float(input("Digite o valor da tensão da fonte em volts:"))
            if tensao_fonte != 0:
                return tensao_fonte
        except ValueError:
            print("Digite apenas números e caso seja decimal utilize ponto, exemplo: 2")
def tensao_dispositivo():
    while True:
        try:
            tensao_dispositivo = float(input("Digite o valor da tensão do dispositivo em volts: "))
            if tensao_dispositivo != 0:
                return tensao_dispositivo
        except ValueError:
            print("Digite apenas números e caso seja decimal utilize ponto, exemplo: 0.2")

def conta_resistencia(tensao, corrente):
    calculo_resistencia = tensao / corrente
    return calculo_resistencia

def conta_corrente(tensao, resistencia):
    calculo_corrente = tensao / resistencia
    return calculo_corrente

def conta_tensao(resistencia, corrente):
    calculo_tensao = resistencia * corrente
    return calculo_tensao

def conta_resistencia_resistor(tensao_fonte, tensao_dispositivo, corrente):
    calculo_resistor = (tensao_fonte - tensao_dispositivo) / corrente
    return calculo_resistor

menu_inicial()
opcao = escolha()

while opcao != 5:

    if opcao == 1:
        resultado = conta_resistencia(tensao(), corrente())
        print("O valor da resistência elétrica em ohms é", resultado)

    elif opcao == 2:
        resultado = conta_corrente(tensao(), resistencia())
        print("O valor da corrente elétrica em ampere é", resultado)

    elif opcao == 3:
        resultado = conta_tensao(resistencia(), corrente())
        print("O valor da tensão em volts é ", resultado)

    elif opcao == 4:
        resultado = conta_resistencia_resistor(tensao_fonte(), tensao_dispositivo(), corrente())
        print("O valor da resistência do resistor em ohms é", resultado)

    menu()
    opcao = escolha()

if opcao == 5:
    print("Você saiu da calculadora!")

