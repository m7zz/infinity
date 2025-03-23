import random

print("===Bem-Vindo!===")

vendas = []

def registrar_vendas():
    print("===preencha os dados a seguir:===")
    while True:
        try:
            nome =  input("digite seu nome: ")
            endereco = input("digite seu CEP: ")
            telefone = input("digite seu numero de telefone: ")
            valor = float(input("digite o valor de sua compra: "))
            break
        except:
            print("digite informacoes validas!")
            print("==" * 30)
  
    venda = {
        'nome' : nome,
        'endereco' : endereco,
        'telefone' : telefone,
        'valor' : valor
    }
    
    vendas.append(venda)

           
while True: 
    registrar_vendas()
    resp = input('Deseja realizar outra venda? [S/N] ')    
    if resp.upper() == 'N': break

print("\n===Vendas registradas===")
for venda in vendas:
    print(f"Nome: {venda['nome']}, Endereço: {venda['endereco']}, Telefone: {venda['telefone']}, Valor: {venda['valor']}")

# Sorteio do brinde
if vendas:
    cliente_sorteado = random.choice(vendas)  # Sorteando uma venda aleatória
    print(f"\nParabéns, {cliente_sorteado['nome']}! Você foi sorteado para receber um brinde!")
else:
    print("\nNão há vendas registradas para o sorteio.")
