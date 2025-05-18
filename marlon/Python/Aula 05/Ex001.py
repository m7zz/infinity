"""1 - Faça um algoritmo utilizando função que 
receba um número e defina se ele é 
- positivo 
- negativo 
ou nulo(0)

Utilizem o return dentro da função de maneira correta """
tst = int(input('Digite o número: '))
def tiponum(num):
    if num > 0:
        return "O número é Positivo"
    elif num < 0:
        return "O número é Negativo"
    else:
        return "O número é Nulo"
    
print(f'O resultado é: {tiponum(tst)}')