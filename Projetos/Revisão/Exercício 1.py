#Solicite um número ao usuário e verifique se ele é positivo ou negativo
print("Vamos solicitar um núemro e o informar se ele é positivo ou negativo")

while True:
    try:
        numero = int(input("Digite um número: "))
    
        if numero == 0:
            print("O número inserido é neutro")

        elif numero < 0:
            print("O número inserido é negativo")

        elif numero > 0:
            print("O número inserido é positivo")
    except ValueError:
        print("Dado inválido, tente novamente utilizando número inteiro, exemeplo: 1")
