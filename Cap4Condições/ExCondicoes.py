# CONDIÇÕES
# ! If - Função que determina que parte do código deve ser considerada e que parte deve ser ignorada.
# ? Sintaxe
  # if <condição>: --> Se a condição for verdadeira
    # bloco verdadeiro --> Execute isso

# ! Else -> É uma a contrapoisção da condição if. 
# ? Sintaxe
  # if <condição>:
    # bloco verdadeiro
  # else: --> Caso contrário...
    # outro bloco 

# ! Elif -> Vem para resolver o problema de vários if aninhados (juntos numa mesmam condição)
# ? Sintaxe
  # if <condição>:
    # bloco verdadeiro
  # elif: <condição>
    # outro bloco 
  # elif <condição>:
    # bloco verdadeiro
  # else: --> Caso contrário...
    # outro bloco 

# Exercício 4.2 - Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 po km acima de 80 km/h
velocidade = float(input("Digite a velocidade: "))
multa = 5.0 * (velocidade - 80)

if velocidade > 80:
  print("Você foi multado.")
  print("O valor da multa é R$ %.2f" % multa)