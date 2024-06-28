#Crie uma função que recebe um nome e escreva uma saudação baseada na hora atual
#Madrugada- 0h até 5h - Boa madrugada
#Manhã- 5h às 12h - Bom dia
#Tarde- 12h às 19h - Boa tarde
#Noite- 19h às 00h - Boa noite

import datetime
tempo = datetime.datetime.now()
hora = tempo.hour
def nome():

    while True:
        try:
            nome = input("Qual o seu nome? ")
            return nome
        except ValueError:
            print("Digite apenas letras!")

if hora >= 5 and hora < 12:
    print("Bom dia", nome())
elif hora >= 12 and hora < 19:
    print("Boa tarde", nome())
elif hora >= 19 and hora < 0:
    print("Boa noite", nome())
elif hora >= 0 and hora < 5:
    print("Boa madrugada", nome())


