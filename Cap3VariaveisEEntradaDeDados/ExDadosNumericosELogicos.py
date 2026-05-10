
# ! Tipos de dados - Numéricos
# Se dividem em: Inteiros (sem parte decimal) e de Ponto Flutuante (com parte decimal)

# ! Tipo de dados - Lógico (booleano)
# Se dividem em: True e False (primeira letra maiúscula)
resultado_verdadeiro = True
resultado_falso = False

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