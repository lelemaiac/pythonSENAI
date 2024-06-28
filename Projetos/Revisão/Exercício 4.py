#Solicite dois números e verifique qual deles é maior e exiba uma mensagem correspondente
print("Vamos solicitar dois números e verificar qual deles é maior")

while True:
    try:
        numero01 = float(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Dado inválido, tente novamente e caso seja um número decimal, utilize ponto, exemplo: 4.5")
while True:
    try:
        numero02 = float(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Dado inválido, tente novamente e caso seja um número decimal, utilize ponto, exemplo: 4.5")
if numero01 > numero02:
    print("O primeiro número é maior que o segundo!")
elif numero02 > numero01:
    print("O segundo número é maior que o primeiro! ")
else:
    print("Dado inválido!")