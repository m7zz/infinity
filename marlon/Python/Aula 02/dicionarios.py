venda = {
    'nome': 'Douglas',
    'idade': 12,
    'CEP': '8473842',
    'valor': '99.99'
}

# Acessando valores
print(venda.get('nome'))  # Saída: Douglas

# Atualizando ou adicionando valores
venda['valor'] = '120.50'
venda['produto'] = 'Camiseta'
print(venda)

# Removendo um valor
venda.pop('produto')
print(venda)

# Limpando o dicionário
venda.clear()
print(venda)  # Saída: {}
