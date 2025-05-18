"""Ex01. Faça um programa que peça as informações de uma pessoa (nome, altura e idade) e armazene em um dicionário, ao final mostre as informações dessa pessoa."""

pessoa = {}    

pessoa['nome'] = input('Digite seu nome: ')
pessoa['altura'] = float(input('Digite sua altura: '))
pessoa['idade'] = int(input('Digite sua idade: '))

print(pessoa)