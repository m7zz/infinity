soma = 0
qtd_numeros = 0
menor = float('inf')
maior = float('-inf')


while True:
    try:
        numero = float(input(f'Digite o {qtd_numeros + 1}º numero: '))

        soma += numero
        qtd_numeros += 1

        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

        resp = input('Deseja continuar? [S/N] ')
        if resp.upper() == 'N': break
    except ValueError:
        print('Digite um número válido')   


media = soma / qtd_numeros

print('-' * 30)
print(f'Quantidade de Numeros: {qtd_numeros}')
print(f'Maior Numero: {maior}')
print(f'Menor Numero: {menor}')
print(f'Soma dos Numeros: {soma}')
print(f'Média dos Numeros: {media}')

