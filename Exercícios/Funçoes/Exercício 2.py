#Conversor de temperatura
#Receber a temperatura em graus celsius e retornar em Kelvin e Fahrenheit

def kelvin(temperatura):
    kelvin = temperatura + 273
    return kelvin

def fahrenheit(temperatura):
    fahrenheit = (temperatura * 1.8) + 32
    return fahrenheit

while True:
    try:
        temperatura = float(input("Digite a temperatura atual: "))
        break
    except ValueError:
        print("Digite apenas números, e caso seja decima utilize ponto. Ex: 22.5")


print("A temperatura atual em Kelvin é:", kelvin(temperatura))

print("A temperatura atual em Fahrenheit é:", fahrenheit(temperatura))

