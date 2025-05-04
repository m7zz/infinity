#faca um programa q peca 3 notas e calcule a media com for e lista.

notas = []

for n in range(3):
    nota = float(input(f'Digite a {n+1}º nota: '))
    notas.append(nota)


# 1°

# qtd_notas = len(notas)
# print('Notas:')
# or n in range(qtd_notas):
#    print(f'- {notas[n]:.2f}')
# ======================================================================================================

# 2°
print('Notas : ')
for nota in notas:
    print(f'- {nota:.2f}')
