produtos = []

def cadastrar_produtos(nome, preco, quantidade):
    produto = {
        'nome': nome,
        'preco' : preco,
        'quantidade': quantidade
    }

    produtos.append(produto)

cadastrar_produtos('Celular', 899.90, 3)
print(produtos)