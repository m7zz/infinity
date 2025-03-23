"""Ex02. Você está fazendo um programa para calcular médias.
O programa deve solicitar ao usuário a quantidade de numeros
e depois pedir essa quantidade.
Ao final, mostre a média dos numeros inseridos.
"""


quantidade = int(input("Digite a quantidade de números: "))


numeros = []


for i in range(quantidade):
    numero = float(input(f"Digite o número {i+1}: "))
    numeros.append(numero)

media = sum(numeros) / quantidade
print(f"\nA média dos números é: {media:.2f}")