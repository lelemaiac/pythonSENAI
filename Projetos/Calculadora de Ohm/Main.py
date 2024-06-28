print("Calculadora de Ohm")
print("Para começarmos precisamos de determinadas informações, coforme listada no menu abaixo")
print(" 1- Resistência elétrica \n 2- Corrente elétrica \n 3- Tensão \n 4- Resistência do resistor")

while True:
    try:
        escolha = int(input("Qual medida você deseja calcular?: "))
        break
    except ValueError:
        print("Dado inválido, tente novamente")


if escolha >= 1 and escolha <= 4:
    while escolha != 0:
        if escolha == 1:
            while True:
                try:
                    voltagem = float(input("Digite o valor da tensão elétrica em volts: "))
                    if voltagem > 0:
                        break
                except ValueError:
                    print("Valor inválido. Digite o valor da tensão elétrica com um número, utilizando o ponto como separador")
            while True:
                try:
                    corrente = float(input("Digite o valor da corrente elétrica em ampere: "))
                    if corrente > 0:
                        break
                except ValueError:
                    print("Valor inválido. Digite o valor da corrente elétrica com um número, utilizando o ponto como separador")
            calculo_resistencia = voltagem / corrente
            print("O valor da resistência é: ", calculo_resistencia, "Ω")

        elif escolha == 2:
            while True:
                try:
                    voltagem = float(input("Digite o valor da tensão elétrica em volts: "))
                    if voltagem > 0:
                        break
                except ValueError:
                    print("Valor inválido. Digite o valor da tensão elétrica com um número, utilizando o ponto como separador")
            while True:
                try:
                    resistor = float(input("Digite o valor da resistência em ohms: "))
                    if resistor > 0:
                        break
                except ValueError:
                    print("Valor inválido. Digite o valor da resistência com um número, utilizando o ponto como separador")
            calculo_corrente = voltagem / resistor
            print("O valor da corrente elétrica é: ", calculo_corrente, "A")

        elif escolha == 3:
            while True:
                try:
                    resistor = float(input("Digite o valor da resistência em ohms: "))
                    if resistor > 0:
                        break
                except ValueError:
                    print("Valor inválido. Digite o valor da resistência com um número, utilizando o ponto como separador")
            while True:
                try:
                    corrente = float(input("Digite o valor da corrente elétrica em ampere: "))
                    if corrente > 0:
                        break
                except ValueError:
                    print("Valor inválido. Digite o valor da corrente com um número, utilizando o ponto como separador")
            calculo_voltagem = resistor * corrente
            print("O valor da tensão elétrica é: ", calculo_voltagem, "V")

        elif escolha == 4:
            while True:
                try:
                    tensao_fonte = float(input("Digite o valor da tensão da fonte em volts: "))
                    if tensao_fonte > 0:
                        break
                except ValueError:
                    print("Valor inválido. Digite o valor da tensão da fonte com um número, utilizando o ponto como separador")
            while True:
                try:
                    tensao_dispositivo = float(input("Digite o valor da tensão do dispositivo em volts: "))
                    if tensao_dispositivo > 0:
                        break
                except ValueError:
                    print("Valor inválido. Digite o valor da tensão do dispositivo com um número, utilizando o ponto como separador")
            while True:
                try:
                    corrente = float(input("Digite o valor da corrente elétrica em ampere: "))
                    if corrente > 0:
                        break
                except ValueError:
                    print("Valor inválido. Digite o valor da corrente elétrica com um número, utilizando o ponto como separador")
            calculo_reistor = (tensao_fonte - tensao_dispositivo) / corrente
            print("O valor da resistência do resistor é: ", calculo_reistor, "Ω")

        print("")
        print(" 1- Resistência elétrica \n 2- Corrente elétrica \n 3- Tensão \n 4- Resistência do resistor")
        while True:
            try:
                escolha = int(input("Qual medida você deseja calcular?: "))
                break
            except ValueError:
                print("Dado inválido, tente novamente")

else:
    print("Os dados inseridos são inválidos")





