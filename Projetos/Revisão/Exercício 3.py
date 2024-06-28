#Solicite o ano de nascimento de uma pessoa, calcule sua idade e verifique se a pessoa é maior ou menor de idade
print("Vamos solicitar o seu ano de nascimento para calcular sua idade e informar se é maior ou menor de idade")
ano_atual = 2024
while True:
    try:
        ano_de_nascimento = int(input("Digite o ano de nascimento: "))
        break
    except ValueError:
        print("Dado inválido, tente novamente com valores inteiros.")
idade = ano_atual - ano_de_nascimento

if idade >= 0 and idade < 18:
    print("Você é menor de idade, pois você tem", idade, "anos")
elif idade >= 18 and idade <= 110:
    print("Você é maior de idade, pois você tem", idade, "anos")
else:
    print("Idade inválida!")