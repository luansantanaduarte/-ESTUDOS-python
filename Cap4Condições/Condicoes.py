# CONDIÇÕES
# ! If - Função que determina que parte do código deve ser considerada e que parte deve ser ignorada.
# ? Sintaxe
  # if <condição>: --> Se a condição for verdadeira
    # bloco verdadeiro --> Execute isso
idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
  print("Seu carro é novo.")
if idade > 3:
  print("Seu carro é velho.")



# ! Else -> É uma a contrapoisção da condição if. 
# ? Sintaxe
  # if <condição>:
    # bloco verdadeiro
  # else: --> Caso contrário...
    # outro bloco 
if idade <= 3:
  print("Seu carro é novo.")
else:
  print("Seu carro é velho.")

# ! Elif -> Vem para resolver o problema de vários if aninhados (juntos numa mesmam condição)
categoria = int(input("Digite a categoria do produto: "))
if categoria == 1:
  preco = 10
elif categoria == 2:
  preco = 18
elif categoria == 3:
  preco = 23
elif categoria == 4:
  preco = 26
elif categoria == 5:
  preco = 31
else: 
  print("Categoria inválida, digite um valor entre 1 e 5!")
  preco = 0

print("O preço do profuto é R$ {:.2f}" .format(preco))

