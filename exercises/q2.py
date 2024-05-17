# as funções print() imprimem o menu linha por linha
# é recomendável colocar seu nome e, em seguida, ajustar o alinhamento das barras verticais
print("|   Bem-vindo à Loja de Gelados [do Fulano | da Fulana])!   |")
print("|-------------------- Cardápio --------------------|")
print("|--------------------------------------------------|")
print("|----- | Tamanho | Cupuaçu (CP) | Açaí (AC) | -----|")
print("|----- |    P    |   R$  9.00   | R$ 11.00  | -----|")
print("|----- |    M    |   R$ 14.00   | R$ 16.00  | -----|")
print("|----- |    G    |   R$ 18.00   | R$ 20.00  | -----|")
print("|--------------------------------------------------|")

# inicializa a variável de valor total ao pedido, que pode incluir múltiplas unidades
valor_total = 0.00

# inicializa as variáveis referentes a um pedido específico
# é extremamente recomendável modificar o nome das variáveis em sua preferência
valor_pedido = 0.00
sabor_pedido = ""
tamanho_pedido = ""


# função para efetuar pedido
# é preferível deixar em formato de função para facilitar na hora de chamar outros pedidos
def fazer_pedido():
    # a chamada global permite chamar as variáveis de escopo global ao escopo da função
    global valor_total
    global sabor_pedido
    global valor_pedido
    global tamanho_pedido
    while True:
        # após pegar o input(), o método .upper() coloca todas as letras em CAPS LOCK
        # dessa forma, fica mais fácil verificar qual sabor o cliente digitou
        sabor_pedido = input("Escolha o sabor desejado (CP ou AC): ").upper()
        # nesse caso, há um array (uma coleção específica de elementos) definido -> ["CP", "AC"]
        # nesse array, existem as duas opções válidas de sabor
        # caso o sabor escolhido pelo cliente não esteja no array (not in), ele avisa que o sabor é inválido
        if sabor_pedido not in ["CP", "AC"]:
            print("Sabor inválido. Tente novamente")
            # a chamada 'continue' faz o loop reiniciar desde o começo
            # ao voltar pro começo, o cliente pode inserir um sabor válido dessa vez
            continue
        else:
            # caso o sabor seja uma opção válida, o break interrompe o loop
            break
            # ao interromper o loop, o código abaixo vai continuar normalmente

    while True:
        tamanho_pedido = input("Entre com o tamanho desejado (P/M/G): ").upper()
        if tamanho_pedido not in ["P", "M", "G"]:
            print("Tamanho inválido. Tente novamente")
            continue
        else:
            break

    # utiliza condicionais para definir o valor do pedido com base no sabor e no tamanho
    # nesse caso, as variáveis globais são modificadas
    if sabor_pedido == "CP":
        if tamanho_pedido == "P":
            valor_pedido = 9.00
        elif tamanho_pedido == "M":
            valor_pedido = 14.00
        elif tamanho_pedido == "G":
            valor_pedido = 18.00
    elif sabor_pedido == "AC":
        if tamanho_pedido == "P":
            valor_pedido = 11.00
        elif tamanho_pedido == "M":
            valor_pedido = 16.00
        elif tamanho_pedido == "G":
            valor_pedido = 20.00

    # valor_total += valor_pedido significa valor_total = valor_total + valor_pedido
    # dessa forma, o valor_total (que começa em zero) é incrementado dinamicamente à medida que o cliente faz pedidos
    valor_total += valor_pedido


# depois de definir as funções, elas ainda não foram chamadas (então o programa não vai executar elas)
# por isso, é importante chamar a função pro cliente fazer o primeiro pedido
fazer_pedido()

# a variável nome_pedido analisa a abreviação para definir o nome
# tradução -> nome_pedido = "Cupuaçu" se o sabor for "CP"; caso contrário, nome_pedido = "Açaí"
nome_pedido = "Cupuaçu" if sabor_pedido == "CP" else "Açaí"

# exibe o pedido feito
print("\nVocê pediu um {} no tamanho {}: R$ {:.2f}".format(nome_pedido, tamanho_pedido, valor_pedido))

# pergunta se o cliente quer fazer outro pedido
while True:
    continuar = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
    if continuar == "S":
        fazer_pedido()  # chama a função de fazer_pedido caso a resposta seja sim
    elif continuar == "N":
        # caso o usuário não queira mais pedidos, interrompe o loop e continua o código fora do While
        break
    else:
        # pergunta de novo caso o usuário escreva algo diferente de S/N
        print("Resposta inválida. Tente novamente (S/N)\n")
        continue

# caso o usuário não queira fazer mais pedidos, exibe o valor total, que foi modificado ao longo do programa
print(f"\nO valor total a ser pago: R$ {valor_total:.2f}")
