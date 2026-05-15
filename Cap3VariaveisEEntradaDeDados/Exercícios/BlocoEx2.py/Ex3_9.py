# Exercícios 3.9 - Escreva um problema que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
horas = int(input("Digite que horas são: "))
horas_segundos = horas * 3600 # Em 1h tem 3600s
minutos = int(input("Quantos minutos? "))
minutos_segundos = minutos * 60 # Em 1min tem 60s
segundos = int(input("E quantos segundos? "))

tempo_total = horas_segundos + minutos_segundos + segundos
print(tempo_total)
