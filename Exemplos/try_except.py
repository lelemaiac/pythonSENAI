# o while repete tudo que está dentro dele
while True:
    try:
        #tentar fazer isso
        idade = int(input("Digite sua idade: "))
        # O if verifica-se idade é válido
        if idade > 0 and idade <= 100:
            print("A idade é: ", idade, "anos")
            # O break sai do while
            break
        else:
            print("Idade inválida")
    except ValueError:
        #Caso der algum erro isso será execeutado
        print("Digite sua idade em número, exemplo: 26")