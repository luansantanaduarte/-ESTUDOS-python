# Exetcício 4.2 - Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 po km acima de 80 km/h
velocidade = float(input("Digite a velocidade: "))
multa = 5.0 * (velocidade - 80)

if velocidade > 80:
  print("Você foi multado.")
  print("O valor da multa é R$ %.2f" % multa)