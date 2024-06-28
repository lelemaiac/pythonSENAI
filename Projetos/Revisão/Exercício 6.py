#Solicite três números inteiros e mostre o maior entre elas
print("Vamos solicitar três números inteiros e informar qual deles é o maior!")
print("")

while True:
    try:
        numero01 = int(input("Digite o primeiro número, sendo inteiro: "))
        break
    except ValueError:
        print("Dado inválido, tente novamente informando através de um número inteiro, exemplo: 8")
while True:
    try:
        numero02 = int(input("Digite o segundo número, sendo inteiro: "))
        break
    except ValueError:
        print("Dado inválido, tente novamente informando através de um número inteiro, exemplo: 8 ")
while True:
    try:
        numero03 = int(input("Digite o erceiro número, sendo inteiro: "))
        break
    except ValueError:
        print("Dado inválido, tente novamente informando através de um número inteiro, exemplo: 8 ")

if numero01 > numero02 and numero01 > numero03:
    print("O maior número entre eles é o primeiro!")
elif numero02 > numero01 and numero02 > numero03:
    print("O maior número entre eles é o segundo!")
elif numero03 > numero01 and numero03 > numero02:
    print("O maior número entre eles é o terceiro!")
else:
    print("Dado inválido!")