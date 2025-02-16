idade = int(input('Qual sua idade? '))

if idade < 16:
    print('Vocẽ não pode votar! ')
elif idade >= 16 and idade < 18:
    print('seu voto é facultativo! ')
elif idade >= 18 and idade < 65:
    print('seu voto é obrigatorio!')
else:
    print('Seu voto é obrigatorio')
    