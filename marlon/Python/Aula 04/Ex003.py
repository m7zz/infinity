# Ex03. A função deve receber uma lista de notas e retornar a média das notas

def media_lista(notas):
    if len(notas) == 0:
        return 0
    
    soma = sum(notas)

    media = soma/len(notas)

    return media

notas = []
quantidade_de_notas = int(input("Quantas notas você quer inserir: "))

for i in range(quantidade_de_notas):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = media_lista(notas)
print(f"A média das notas é: {media}")