#Solicite um número de 1 a 12 representados em meses do ano
print("Vamos solicitar um número entre 1 e 12 para representar em meses do ano")
while True:
    try:
        numero = int(input("Digite um número entre 1 e 12 para representar em meses do ano: "))
        if numero >= 1 or numero <= 12:
            break
    except ValueError:
        print("Dado inválido, digie um número entre 1 e 12, sendo inteiro!")
if numero == 1:
    print("Esse número corresponde a Janeiro!")
elif numero == 2:
    print("Esse número corresponde a Fevereiro!")
elif numero == 3:
    print("Esse número corresponde a Março!")
elif numero == 4:
    print("Esse número corresponde a Abril!")
elif numero == 5:
    print("Esse número corresponde a Maio!")
elif numero == 6:
    print("Esse número corresponde a Junho!")
elif numero == 7:
    print("Esse número corresponde a Julho!")
elif numero == 8:
    print("Esse número corresponde a Agosto!")
elif numero == 9:
    print("Esse número corresponde a Setembro!")
elif numero == 10:
    print("Esse número corresponde a Outubro!")
elif numero == 11:
    print("Esse número corresponde a Novembro!")
elif numero == 12:
    print("Esse número corresponde a Dezembro!")
else:
    print("Dado inválido!")
