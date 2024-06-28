#Solicite ao usuário o valor de sua renda anual bruta e em seguida, exiba o desconto do seu salário no emposto de renda
print("Vamos solicitar sua renda bruta anual para vermos quanto do seu salário será descontado!")
desconto = 0

while True:
    try:
        renda = float(input("Digite a renda bruta anual: "))
        break
    except ValueError:
        print("Dado inválido, tente novamente com número, e caso seja decimal utilize o ponto, exemplo: 2.5!")

if renda >= 0 and renda <= 56072.00:
    print("De acordo com o valor inserido não será descontado o imposto de renda do seu salário!")

#7,5%
elif renda >= 56072.01 and renda <= 238532.00:
    desconto = renda * 0.075
    print("Será descontado ", desconto, " do seu salário!")

#15%

elif renda >= 238532.01 and renda <= 522400.00:
    desconto = renda * 0.15
    print("Será descontado ", desconto, " do seu salario!")
#22,5%

elif renda >= 522400.01 and renda <= 9876000.00:
    desconto = renda * 0.225
    print("Será descontado ", desconto, " do seu salario!" )

elif renda >= 9876000.01:
    desconto = renda * 0.275
    print("Será descontado ", desconto, " do seu salario!")