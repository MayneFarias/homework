lista_livro = []
id_global = 0


def cadastrar_livro(id):
    global id_global
    id_global += 1
    nome = input("Escolha o nome do livro: ")
    autor = input("Escolha o nome do autor: ")
    editora = input("Escolha o nome da editora: ")
    livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livro.append(livro)


def consultar_livro():
    while True:
        print("Consultar Livro:")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu")
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            for livro in lista_livro:
                print(f"Livro: [ Nome: {livro['nome']} "
                      f"| ID: {livro['id']} "
                      f"| Autor: {livro['autor']} "
                      f"| Editora: {livro['editora']} ]\n")
        elif opcao == 2:
            id_consulta = int(input("Digite o ID do livro desejado: "))
            for livro in lista_livro:
                if livro['id'] == id_consulta:
                    print(f"Livro: [ Nome: {livro['nome']} "
                          f"| ID: {livro['id']} "
                          f"| Autor: {livro['autor']} "
                          f"| Editora: {livro['editora']} ]\n")
                    break
            else:
                print("Livro não encontrado.")
                break
        elif opcao == 3:
            autor_consulta = input("Digite o nome do autor desejado: ")
            for livro in lista_livro:
                if livro['autor'] == autor_consulta:
                    print(f"Livro: [ Nome: {livro['nome']} "
                          f"| ID: {livro['id']} "
                          f"| Autor: {livro['autor']} "
                          f"| Editora: {livro['editora']} ]\n")
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente")
            continue


def remover_livro():
    while True:
        id_livro_para_remover = int(input("Digite o ID do livro que quer remover ou digite 0 para voltar ao menu: "))
        if id_livro_para_remover == 0:
            break
        for livro in lista_livro:
            if livro['id'] == id_livro_para_remover:
                lista_livro.remove(livro)
                print("Livro '{}' removido.".format(livro['nome']))
                break
        else:
            print("ID inválido. Tente novamente")
            continue


print("Bem vindo à livraria [do Fulano | da Fulana]!")
while True:
    print("\nMenu Principal:")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro")
    print("3 - Remover Livro")
    print("4 - Encerrar Programa")
    escolha_menu_principal = int(input("Escolha uma opção: "))

    if escolha_menu_principal == 1:
        print("")
        cadastrar_livro(id_global + 1)
    elif escolha_menu_principal == 2:
        print("")
        consultar_livro()
    elif escolha_menu_principal == 3:
        print("")
        remover_livro()
    elif escolha_menu_principal == 4:
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida.")
        continue
