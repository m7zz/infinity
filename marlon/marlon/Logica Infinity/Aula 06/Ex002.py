"""Ex02. Faça um programa que pede um numero para o usuário, e mostre o enésimo valor da sequencia de fibonacci. Exemplo:
Até qual numero deseja mostrar fibonacci? 
>>> 8
0 1 1 2 3 5 8 13
OBS: a sequencia de fibonacci começa com "0" e "1" e o proximo termo é a soma dos dois anteriores."""

def fibonacci(n):
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a
try:
    n = int(input("Digite um número: "))
    print(fibonacci(n))
except ValueError:
    print('Por favor digite um valor válido')