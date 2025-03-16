ano = int(input('Digite o ano: '))

sim1 = ano % 4
sim2 = ano % 100
sim3 = ano % 400

if sim1 == 0 and (sim2 != 0) or sim3 == 0:
    print('Digamos que o ano é bissexto')
else:
    print('DIgamos que o ano não é bissexto')