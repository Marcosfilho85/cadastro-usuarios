from usuarios import adicionar_usuario, listar_usuarios, buscar_usuario

def menu():
    while True:
        print("\n=== SISTEMA DE CADASTRO ===")
        print("1 - Adicionar usuário")
        print("2 - Listar usuários")
        print("3 - Buscar usuário")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome: ")
            idade = input("Idade: ")
            adicionar_usuario(nome, idade)

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "3":
            nome = input("Digite o nome: ")
            buscar_usuario(nome)

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

menu()
