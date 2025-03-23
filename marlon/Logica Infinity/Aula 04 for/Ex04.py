print('Contador de Vogais!')
texto = input('Digite um texto: ')

qtd_vogais = 0

for letra in texto:
  if letra.upper() in 'AEIOU':
        qtd_vogais += 1

print(f'A quantidade de vogais é : {qtd_vogais}')