usuarios = []

def adicionar_usuario(nome, idade):
    usuario = {
        "nome": nome,
        "idade": idade
    }
    usuarios.append(usuario)

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for i, u in enumerate(usuarios, 1):
            print(f"{i}. {u['nome']} - {u['idade']} anos")

def buscar_usuario(nome):
    for u in usuarios:
        if u["nome"].lower() == nome.lower():
            print(f"Encontrado: {u['nome']} - {u['idade']} anos")
            return
    print("Usuário não encontrado.")
