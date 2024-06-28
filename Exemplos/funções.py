from datetime import datetime

def menu_calculadora():
    print("Menu calculadora")
    print("1- Adição")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")

def ola_nome(nome):
    print("Olá", nome)

while True:
    try:
        nome = input("Qual o seu nome? ")
    except ValueError:
        print("Dado inválido, insira somente letras")

ola_nome(nome)

def calcule_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade
print("Sua idade é", calcule_idade(2008), "anos")


#menu_calculadora()