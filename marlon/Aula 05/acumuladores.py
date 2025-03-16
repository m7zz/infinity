qtd_maior_de_idade = 0
qtd_menor_de_idade = 0

for p in range(5):
    idade = int(input('Digite a sua idade: '))

    if idade >= 18:

        qtd_maior_de_idade += 1
    else:
        qtd_menor_de_idade += 1

print(f'Temos exatos {qtd_maior_de_idade} maiores de idade.')
print(f'Temos exatos {qtd_menor_de_idade} menores de idade.')