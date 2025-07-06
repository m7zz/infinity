try:
    numero = float(input('Digite um numero: '))
    print (numero)

except ValueError:
    print('Digite um número valido.')

finally:
    print('Sempre fui chamado')