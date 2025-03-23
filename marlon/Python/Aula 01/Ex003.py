#Ex03. Faça um programa que peça 6 numeros e armazene-os em uma lista. Ao final, mostre a soma entre os numeros.

numeros = []

for n in range (6):
    numero = int(input(f'Digite o {n+1}º número: '))
    numeros.append(numero)

print('numeros:')
print(f'- {numeros}')   

soma = sum(numeros)
print(f'A soma dos números é {soma}')