#Solicite duas notas a um aluno e calcule sua média, caso seja maior ou igual a 70, o aluno será aprovado
#Caso seja menor está reprovado
print("Vamos solicitar duas notas para poder calcular sua média e informar se está aprovado ou reprovado.")

while True:
    try:
        nota01 = float(input("Digite a primeira nota: "))
        if nota01 >= 0 and nota01 <= 100:
            break
    except ValueError:
        print("Dado inválido, utilize apenas números e caso seja decimal, utilize ponto, exemplo: 2.0")
while True:
    try:
        nota02 = float(input("Digite a segunda nota: "))
        if nota02 >= 0 and nota02 <= 100:
            break
    except ValueError:
        print("Dado inválido, utilize apenas números e caso seja decimal, utilize ponto, exemplo: 2.0")

soma = nota01 + nota02
media = soma / 2
if media >= 0 and media < 70:
    print("Você foi reprovado, pois ficou com a média", media)

elif media >= 70 and media <= 100:
    print("Você foi aprovado, pois sua média ficou", media)

