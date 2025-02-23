"""
Ex03. Faça um programa onde o usuário irá fazer uma contagem
e ele irá informar o Inicio, o Final e o Passo da contagem.
"""

valor = int(input('Digite até onde vai contar: '))
inicio = int(input('Digite o inicio da contagem: '))
passo = int(input('Digite a quantidade de passos: '))


for numero in range(inicio,valor + 1,passo):
    print(numero)  