"""Ex03. Faça um programa que peça um texto para o usuário e crie um dicionário que irá conter todas as letras e suas respectivas quantidades, exemplo:

Entrada:
>>> Digite um Texto: Casa

Saída:
{
    'c': 1,
    'a': 2,
    's': 1
}
"""
print("----Contador de palavras ----")

texto = input('Digite o texto aqui: ').lower()
dicionario = {}

for letra in texto:
    if letra.isalpha():
        if letra in dicionario:
            dicionario[letra] += 1
        else:
            dicionario[letra] = 1

for letra in dicionario:
    print(f'{letra.upper()} : {dicionario[letra]}')

print(f"A palavra digitada foi: {texto}")