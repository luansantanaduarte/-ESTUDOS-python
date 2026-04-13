# VÁRIAVEIS
# ! Tipos de dados - Numéricos
# Se dividem em: Inteiros (sem parte decimal) e de Ponto Flutuante (com parte decimal)

# ! Tipo de dados - Lógico (booleano)
# Se dividem em: True e False (primeira letra maiúscula)
resultado_verdadeiro = True
resultado_falso = False
# Existem operações relacionais que retornam um valor booleano
a = 1 
b = 5
c = 2
d = 1

print(a == b) # a é igual a b? False
print(b > a) # b é maior que b? True
print(a < b) # a é menor que b? True
print(a >= b) # a é maior ou igual a b? False
print(c <= b) # a é menor ou igual a b? True
print(d != a) # d é diferente de a? False

# ! Operadores lógicos
# São operadores que permitem a realização de operações com lógica booleana. São eles: 
# * not (não - negação), and (e - conjunção), or (ou - disjunção)

# Operador not - inverte o valor lógico.
print(not False)

# Operador and - resultado verdadeiro, somente quando ambas as proposições são verdadeiras.
print(True and True) # <- único caso verdadeiro.

# Operador or - resultado falso, somente quando ambas as proposições forem falsas.
print(False or False) 
print(True or False) # <- Se, ao menos uma proposição for verdadeira, a operação resulta em verdadeiro.

# No caso de expressões lógicas, a ordem a ser avaliada é:
# 1º) Operação not
# 2º) Operação and
# 3º) operação or

# ! Tipo de dados - String
# * String - Conjunto de caractéres. É delimitado por aspas ("").
# Variáveis do tipo string armazenam caracteres de texto (nomes, números, sinais de pontuação...).

# * Função len -> Responsável por retornar o número de caractéres de uma string.
# ? Sintaxe -> len(string)
print(len("A"))
print(len(""))
print(len("O rato roeu a roupa")) # Conta com os espaços

# É possível acessar um determinado elemento da string a partir de um número inteiro que representa seu ordenamento (índice).
# Começamos a contar do número 0 e o último é o número total - 1 ou len(string) - 1.
# ? Sintaxe -> variável[número do índice]
a = "ABCDEF"
print(a[0])
print(a[1])

# ! print(a[6])
# Erro -> Obtido quando o número do índice é maior que o número total de caractéres.
# Traceback (most recent call last):
#   File "c:\Users\lsant\OneDrive\Documentos\Luan\Faculdade\IPComPython\Cap3\VariáveisELogicaBooleana.py", line 57, in <module>
#     print(a[6])
#           ~^^^
# IndexError: string index out of range


# Operações com strings.
# Concatenação - "Soma de strings" ou a união de duas ou mais strings.
s = "ABC"
print(s + "C")
# A multiplicação também é possível.
print(s + "D" * 4) # Nesse caso, indicamos que a string "D" vai se repetir 4x.
print("X" + "-" * 10)

# Composição - União dois elementos de tipos diferentes.
# Uma vez que fazer print("Luan tem" + 19), fazemos:
# ? Sintaxe -> "João tem %d anos % X" (o d representa que a substituição será por um número inteiro)
idade = 19
print("João tem %d anos" % idade)

# O uso do % pode se dá para formatar números.
x = 22
print("[%03d]" % x) # Formata o número com no mínimo 3 algarismos, independente do número formado.
print("[%3d]" % x) # Formata o número com um espaço (caso o número não tenha 3 algarismos).
print("[%-3d]" % x) # Formata o número com um espaço a direita (independente do número formado).

# Com números decimais, podemos usar para formatar quantos números queremos após a vírgula.
valor = 5
print("R$ %f" % valor) # Utilização do número decimal. 
# Para personalizar a quantidade fazemos:
print("R$ %.2f" % valor) # ? Sintaze -> "%.(número de casas)f"

# Podemos mudar mais de um valor.
print("%s tem %d anos e apenas R$ %.2f no bolso." % ("Lucas", 22, 51.34))
# Forma mais moderna -> format().
nome = "João"
anos = 22
grana = 51.34656
# : valor - delimita espaçamento após o texto e o .valor determina quantas casas após a vírgula terá.
print("{:12} tem {:<3} anos e R$ {:8.2f} no bolso." .format(nome, idade, grana))

# Fatiamento - Fazer a remoção de uma porção da string.
# ? Sintaxe -> variavel[posição inicial: posição final]
z = "ABCDEFGHI"
print(z[0:2]) # Fatiamento da posição 0 a 1 (não inclui a posição 2).
# Podemos omitir o início ou fim indicando que são todos os termos até determinado ponto.
print(z[2:])
# Números negativos podem ser usados para representar os valores a contar do último até o primeiro (-1 - último, -2 - penúltimo...).



