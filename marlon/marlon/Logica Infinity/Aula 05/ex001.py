"""Ex01. Faça um programa que peça 3 numeros para o usuário
e mostre a soma dos numeros (utilizando o FOR).
"""

soma = 0

for n in range(3):
    numero=int(input(f'Digite um numero: '))
    soma += numero

print(soma)