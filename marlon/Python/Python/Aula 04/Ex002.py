#calcule 3 notas e mostra a media com def.

def calcular_media(nota1,nota2,nota3):
    media = (nota1 + nota2+ nota3) / 3
    return media

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))

media_total = calcular_media(n1, n2, n3)
print(f'a media das notas é : {media_total}')