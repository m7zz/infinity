# Ex02. Faça um programa que peça 5 nomes e mostre todos os nomes digitados
nomes = []

for nome in range (5):
    nome = input(f'Digite o {nome+1}º nome: ')
    nomes.append(nome)

print('-----Nomes Cadastrados -----')
print(f'- {nomes}')