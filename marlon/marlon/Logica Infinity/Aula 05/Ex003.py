"""Ex03. Faça um programa que peça 5 numeros para o usuário
e mostre o maior numero inserido."""

maior = None

for i in range(5): # passos e quantidade
    try:
        numero = int(input(f"Digite o número {i+1}: "))
    
        if maior == None or numero > maior :
            maior = numero
    except ValueError:
        print('Digite um número válido!')
print(f'O maior número é {maior}')
