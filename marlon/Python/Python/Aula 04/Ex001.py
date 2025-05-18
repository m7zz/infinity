"""
Ex01. Faça uma função chamda "multiplicar" que recebe dois numeros e retorna o produto (multiplicação) entre eles."""

def multiplicar(n1, n2):
    return n1 * n2

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))

resultado = multiplicar(num1, num2)

print(f'O resultado é: {resultado}')