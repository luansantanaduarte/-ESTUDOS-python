# Exerício 3.7 - Faça um programa que peça dois números inteiros. Imprima a soma desses dois números na tela
n1 = float(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
print(n1 + n2)

# Exercícios 3.8 - Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
# Sabendo que 1m = 1000 mm, fazemos:
metro = float(input("Digite o tamanho em metros: "))
milimetros = metro * 1000
print(milimetros) 

# Exercícios 3.9 - Escreva um problema que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
horas = int(input("Digite que horas são: "))
horas_segundos = horas * 3600 # Em 1h tem 3600s
minutos = int(input("Quantos minutos? "))
minutos_segundos = minutos * 60 # Em 1min tem 60s
segundos = int(input("E quantos segundos? "))

tempo_total = horas_segundos + minutos_segundos + segundos
print(tempo_total)
