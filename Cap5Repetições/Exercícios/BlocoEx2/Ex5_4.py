# Pág. 87
# Exercício 5.4 - Modifique o programa para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os número ímpares.
limite = int(input("Digite até onde a contagem vai: "))
x = 0
while x <= limite:
  if x % 2 != 0:
    print(x)
  x += 1