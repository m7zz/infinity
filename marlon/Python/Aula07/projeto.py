produtos = []

def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de Produtos:")
        for i, p in enumerate(produtos, start=1):
            print(f"{i}. Nome: {p['nome']} | Preço: R${p['preco']:.2f} | Quantidade: {p['quantidade']}")
    print()

def cadastrar_produto():
    nome = input('Digite o nome do novo produto: ')
    preco = float(input('Digite o preço do produto: '))
    quantidade = int(input('Digite a quantidade do novo produto: '))
    
    produto = {
        'nome' : nome,
        'preco' : preco,
        'quantidade' : quantidade
    }
    produtos.append(produto)

    print('Produto Cadastrado com sucesso') 


def editar_produto():
    listar_produtos()
    try:
        index = int(input("Digite o número do produto a editar: ")) - 1
        if 0 <= index < len(produtos):
            produtos[index]['nome'] = input("Novo nome: ")
            produtos[index]['preco'] = float(input("Novo preço: R$"))
            produtos[index]['quantidade'] = int(input("Nova quantidade: "))
            print("Produto editado com sucesso!\n")
        else:
            print("Produto inválido.\n")
    except ValueError:
        print("Entrada inválida.\n")

def excluir_produto():
    listar_produtos()
    try:
        index = int(input("Digite o número do produto a excluir: ")) - 1
        if 0 <= index < len(produtos):
            produtos.pop(index)
            print("Produto excluído com sucesso!\n")
        else:
            print("Produto inválido.\n")
    except ValueError:
        print("Número Invalido\n")

def menu():
    while True:
        print("""
=================================
     Gerenciamento de Produtos 
================================= 
[1] - 📃 Listar Produtos
[2] - ➕ Cadastrar Produto
[3] - ✏️ Editar Produto
[4] - ❌ Excluir Produto
[5] - Criador
[6] - 🚪 Sair

=====================================
""")
        opcao = input("--> Selecione uma Opção: ")

        if opcao == '1':
            listar_produtos()
        elif opcao == '2':
            cadastrar_produto()
        elif opcao == '3':
            editar_produto()
        elif opcao == '4':
            excluir_produto()
        elif opcao == '5':
            print("Dados do criador: \n Nome: Marlon \n Instagram: m7rlon.zy \n GitHub: m7zz \n")
            break 
        elif opcao == '6':
            print("Encerrando programa")
            break
        else:
            print("Opção inválida!\n")

menu()