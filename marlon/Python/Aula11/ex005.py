class Fatura:
    def __init__(self, nome_item, preco_unitario, quantidade):
        self.nome_item = nome_item
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.valor_total = 0

    def gerar_fatura(self):
        self.valor_total = self.preco_unitario * self.quantidade
        return self.valor_total

# Pedir dados ao usuário
nome_item = input("Digite o nome do item: ")
preco_unitario = float(input("Digite o preço unitário do item: "))
quantidade = int(input("Digite a quantidade do item: "))

# Criar o objeto e gerar a fatura
fatura = Fatura(nome_item, preco_unitario, quantidade)
total = fatura.gerar_fatura()

print(f"O valor total da fatura para '{nome_item}' é: R$ {total:.2f}")
          