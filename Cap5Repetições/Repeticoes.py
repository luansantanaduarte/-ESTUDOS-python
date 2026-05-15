# Capítulo 5 - Repetições 
# Vem com o objetivo de repetir partes de código que dariam incontáveis linhas de maneira mais simples.

# ! While -> Repetição de um bloco de código enquanto determinada condição for verdadeira.
# ? Sintaxe:
  # while <condicao>:
    # bloco de código

# ----------- Exemplo ----------- 
# Código que imprime de 1 a 3 na tela.
# x = 1 
# while x <= 3:  Aqui a condição é reavaliada a cada ciclo.
#  print(x)
#  x += 1  Acrescemos o valor de x até o número 3 e posteriormente 4 quando a condição = false.

# ! Contadores -> Váriaveis que contam a ocorrência de determinado evento.
# ----------- Exemplo ----------- 
# fim = int(input("Digite o último número a imprimir "))
# x = 1
# while x <= fim:
#  print(x)
#  x += 1

# * É possível utilizar estruturas de repetição para filtrar as possíveis saídas.
# ----------- Exemplo ----------- 
# Impressão de números pares de 0 a um número escolhido pelo usuário.
# fim = int(input("Digite o úlitmo número a imprimir: "))
# x = 0
# while x <= fim:
#  if x % 2 == 0:
#    print(x)
#  x += 1
