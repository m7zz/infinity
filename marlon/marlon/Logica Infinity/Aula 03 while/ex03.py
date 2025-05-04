contador = 0
soma = 0

while contador < 3:
    numero = float(input('Digite um número: '))
    soma += numero
    contador += 1

print(f'A soma dos números é: {soma}')