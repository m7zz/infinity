"""Ex01. Faça um programa que peça umm numero e diga se esse número é primo ou não
OBS: Lembrando que um número primo é divisivel somente por 1 e por ele mesmo"""

numero = int(input('Digite um número: '))
primo = numero > 1

for i in range(2, numero): 
    if numero % i == 0:
        primo = False
        break

if primo == True:
    print(f'O {numero} é primo')
else:
    print(f'O {numero} não é primo')

