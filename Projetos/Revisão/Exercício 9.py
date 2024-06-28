#Utilize a biblioteca datetime para mostrar o ano, mês e dia da semana e pegar o horário atual
#Dar uma saudação ao usuário

#datetime biblioteca de tempo/data

import datetime

tempo = datetime.datetime.now()
hora = tempo.hour
minuto = tempo.minute
dia = tempo.day
mes = tempo.month
ano = tempo.year
dia_semana = tempo.strftime("%A")

if hora >= 6 and hora < 12:
    print("Bom dia!")
elif hora >= 12 and hora < 18:
    print("Boa tarde!")
elif hora >= 18 and hora < 6:
    print("Boa noite!")

if mes == 1:
    mes = "Janeiro"
elif mes == 2:
    mes = "Fevereiro"
elif mes == 3:
    mes = "Março"
elif mes == 4:
    mes = "Abril"
elif mes == 5:
    mes = "Maio"
elif mes == 6:
    mes = "Junho"
elif mes == 7:
    mes = "Julho"
elif mes == 8:
    mes = "Agosto"
elif mes == 9:
    mes = "Setembro"
elif mes == 10:
    mes = "Outubro"
elif mes == 11:
    mes = "Novembro"
elif mes == 12:
    mes = "Dezembro"

if dia_semana == "Sunday":
    dia_semana = "um domingo"
elif dia_semana == "Monday":
    dia_semana = "uma segunda"
elif dia_semana == "Tuesday":
    dia_semana = "uma terça"
elif dia_semana == "Wednesday":
    dia_semana = "uma quarta"
elif dia_semana == "Thursday":
    dia_semana = "uma quinta"
elif dia_semana == "Friday":
    dia_semana = "uma sexta"
elif dia_semana == "Saturday":
    dia_semana = "um sábado"

print(f"Hoje é dia {dia} de {mes} de {ano} {dia_semana}")

