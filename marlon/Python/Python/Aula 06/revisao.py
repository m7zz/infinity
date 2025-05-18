def mostrar_produtos(nome, preco, quantidade):
    print(f"Produto : {nome}")
    print(f"Preço : R${preco:.2f}")
    print(f"Quantidade: {quantidade}")

n1 = input("O nome do produto: ")
p1 = float(input("Digite o preço do produto: "))
q1 = int(input("Digite a quantidade dos produtos: "))

mostrar_produtos(n1, p1, q1)