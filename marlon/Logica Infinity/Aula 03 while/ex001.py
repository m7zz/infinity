"""Revisão: Faça um programa que peça 3 notas, calcule a média e mostre a situação do aluno:

APROVADO -> Media maior ou igual a 6
RECUPERACAO -> Media maior ou igual a 4 e menor que 6
REPROVADO -> Media menor que 4"""

nota1 = float(input('Digite a 1° nota do aluno: '))
nota2 = float(input('Digite a 2° nota do aluno: '))
nota3 = float(input('Digite a 3° 1nota do aluno: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print('O aluno foi aprovado!')
elif media >= 4 and media < 6:
    print('O aluno está de recuperação')
else:
    print('O aluno foi reprovado!')

print(f"A media da lenda foi: {media:.2f}")