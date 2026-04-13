# Exercício 3.4 - Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que R$1200,00
salario = 1200
pagante = salario > 1200

# Exercício 3.5 - Calcule o restulado da expressão A > B and C or D utilizando os valores da tabela a seguir (página 60).
# A = 1, B = 2, C = True e D = False
a1 = 1
b1 = 2
c1 = True
d1 = False
verificacao1 = a1 > b1 and c1 or d1
print(verificacao1)

# A = 10, B = 3, C = False e D = True
a2 = 10 
b2 = 3
c2 = False
d2 = False
verificacao2 = a2 > b2 and c2 or d2
print(verificacao2)

# A = 5, B = 1, C = True e D = True
a3 = 5
b3 = 1
c3 = True
d3 = True
verificacao3 = a3 > b3 and c3 or d3
print(verificacao3)