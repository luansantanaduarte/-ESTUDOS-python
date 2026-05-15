# Pág. 88
# Exercício 5.6 - Criar um tabuada que imprima o a operação e o resultado: 2x1 = 2...
numero = int(input("Digite o número e descubra a tabuada: "))
x = 0 
while x <= 10:
  resultado =  numero * x
  print("%s x %d = %d" % (numero, x, resultado))
  print("{} x {} = {}" .format(numero, x, resultado))
  x += 1