# questão 1/4

# função print() para exibir uma mensagem que inclui seu nome!
print("Bem-vindo à loja [do Fulano | da Fulana]")

# o método input() recebe o valor que o usuário digitar no terminal
# o método int() converte o valor digitado pelo usuário em um numero inteiro (tipo primitivo int)
# o valor convertido pelo método int() é armazenado em uma variável
valor_do_produto = int(input("Coloque o valor do produto: "))

# o valor convertido pelo método int(input()) é armazenado em uma variável
quantidade_de_produtos = int(input("Coloque a quantidade de produtos: "))

# o produto do valor do produto pela quantidade de produtos é armazenado em uma variável
valor_total = valor_do_produto * quantidade_de_produtos

# a variável desconto é definida em valor global (para ser acessada dentro e fora de blocos de código)
# essa variável é inicializada com o valor 0.00, então o python atribui o tipo de dado 'floating point'
# exemplos de floating points: 11.5, 99.35, 2699.99
desconto = 0.00

# bloco condicional para verificar o valor total (definido previamente)
# com base no valor total, a variável desconto (definida globalmente) vai ser modificada
if valor_total >= 2500 and valor_total < 6000:
    desconto = 4/100  # desconto de 4%
elif valor_total >= 6000 and valor_total < 10000:
    desconto = 7/100  # desconto de 7%
elif valor_total >= 10000:
    desconto = 11/100  # desconto de 11%
# caso nenhum bloco condicional acima seja executado, o código executará o 'else'
# nesse caso, o valor só pode ser menor do que 2500 e, portanto, não receberá redução nenhuma (desconto zerado)
else:
    desconto = 0

# {:.2f} identa o valor numérico para que ele seja exibido com duas decimais de precisão
# o método .format() atribui os parâmetros que ele recebe dentro dos parênteses aos placeholders (as chaves { })
print("O valor total do pedido SEM desconto é: R$ {:.2f}".format(valor_total))
print("O valor total do pedido COM desconto é: R$ {:.2f}".format(valor_total * (1 - desconto)))
