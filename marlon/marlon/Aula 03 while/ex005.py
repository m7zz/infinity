"""Ex05. Faça um programa que peça varios numeros, e após cada numero pergunte se o usuário deseja continuar (ele deve responder 'S' para Sim e 'N' para Não), quando essa resposta for 'N' você deve parar a repetição e mostrar a média dos numeros digitados.
"""

soma = 0
contador = 0

while True:
    numero = float(input('Digite um número: '))
    soma += numero
    contador += 1
    continuar = input('Deseja continuar? S para continuar e N para parar!: ')
    if continuar == 'S, s'or continuar == 's':
        continue
    elif continuar == 'N' or continuar == 'n':
        break
    else:
        print("Digite S ou N! ")
        break



    
media = soma / contador 
print(f'A media dos números é: {media}')