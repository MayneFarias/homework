print("| Bem-vindo à Copiadora [do Fulano | da Fulana] |")


def escolha_servico():
    print("Selecione o serviço desejado")
    print("DIG - Digitalização")
    print("ICO - Impressão Colorida")
    print("IPB - Impressão Preto e Branco")
    print("FOT - Fotocópia")
    while True:
        servico = input(">> ").upper()
        if servico not in ["DIG", "ICO", "IPB", "FOT"]:
            print("Opção inválida. Tente novamente")
            continue
        else:
            if servico == "DIG":
                return 1.10
            elif servico == "ICO":
                return 1.00
            elif servico == "IPB":
                return 0.40
            else:
                return 0.20


def num_pagina():
    desconto = 0.00
    num_paginas = 0.00
    while True:
        try:
            num_paginas = int(input("Selecione o número de páginas: "))
            if 20000 <= num_paginas:
                print("Não aceitamos tantas páginas de uma vez.")
                continue
            if 20 <= num_paginas < 200:
                desconto = 0.15
                break
            elif 200 <= num_paginas < 2000:
                desconto = 0.20
                break
            elif 2000 <= num_paginas < 20000:
                desconto = 0.25
                break
            else:
                desconto = 0
                break
        except ValueError:
            print("Opção inválida. Tente novamente")
            continue
    return num_paginas * (1 - desconto)


def servico_extra():
    print("Deseja algum serviço adicional?")
    print("1 - Encadernação simples")
    print("2 - Encadernação de capa dura")
    print("0 - Não desejo serviço adicional\n")
    while True:
        try:
            extra = int(input(">> "))
            if extra not in [1, 2, 0]:
                print("Opção inválida. Tente novamente")
                continue
            if extra == 1:
                return 15
            elif extra == 2:
                return 40
            else:
                return 0
        except ValueError:
            print("Opção inválida. Tente novamente")
            continue


valor_servico = escolha_servico()
numero_de_paginas = num_pagina()
valor_servico_extra = servico_extra()
print(f"\nTotal: R$ {((valor_servico * numero_de_paginas) + valor_servico_extra):.2f}")
