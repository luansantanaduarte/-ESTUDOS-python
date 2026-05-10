
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

# ? Forma mais moderna -> format().
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

# Sequência de tempo - Váriáveis podem mudar de valor ao longo do código.

# Rastreamento - Capacidade de analisarmos linha a linha um programa buscando erros ou incoerências.

# ! Entrada de dados
# Capacidade de obtermos dados de fora do código, a partir do usário ou arquivo.
# * Função input() -> Responsável por recolher a mensagem do usuário 
# ? Sintaxe -> input("Texto a ser exibido")
nome = input("Digite seu nome ")
print("Você digitou %s" % nome)  # Utilização da composição
print("Olá, {}" .format(nome)) # Utilização do .format

# A função input sempre retorna um valor em string. Para realizar as transformações fazemos:
anos = int(input("Anos de serviço: ")) # Transforma a string em int. O mesmo se aplica para float() ou str()




