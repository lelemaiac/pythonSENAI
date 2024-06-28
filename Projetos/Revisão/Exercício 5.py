#Solicite um número de 1 a 7 representados em dias da semana
print("Vamos solicitar um número entre 1 e 7 para representar em dias da semana")
while True:
    try:
        numero = int(input("Digite um número entre 1 e 7 para representarmos em dias da semana: "))
        if numero >= 1 or numero <= 7:
            break
    except ValueError:
        print("Dado inválido, digie um número entre 1 e 7, sendo inteiro!")
if numero == 1:
    print("Esse número corresponde a domingo!")
elif numero == 2:
    print("Esse número corresponde a segunda!")
elif numero == 3:
    print("Esse número corresponde a terça")
elif numero == 4:
    print("Esse número corresponde a quarta!")
elif numero == 5:
    print("Esse número corresponde a quinta!")
elif numero == 6:
    print("Esse número corresponde a sexta!")
elif numero == 7:
    print("Esse número corresponde a sábado!")
else:
    print("Dado inválido!")