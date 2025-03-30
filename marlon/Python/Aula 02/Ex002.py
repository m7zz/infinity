"""
Ex02. Faça um programa que peça o nome e 3 notas de um aluno, essas informações devem ser salvas em um dicionário com as chaves "nome" e "notas" (notas deve ser uma lista com as 3 notas). 

Depois, calcule a média do aluno e sua situação (APROVADO se a nota for maior ou igual a 6, se não reprovado) e armazene essas informações em 2 novas chaves

Ao final mostre todas as informações do aluno."""


def dados_aluno():
    
    aluno = {}

    aluno['nome'] = input("Digite o nome do aluno: ")
    aluno['notas'] = []

    for i in range(3):

        nota = float(input(f"Digite a {i+1}ª nota: "))
        aluno['notas'].append(nota)

    media = sum(aluno['notas']) / len(aluno['notas'])
    aluno['media'] = media

    if media >= 6:
        aluno['situacao'] = 'O aluno foi aprovado'
    else:
        aluno['situacao'] = 'O aluno foi reprovado'
    return aluno

def mostrar_dados_aluno(aluno):
    print("\nInformações do Aluno:")
    print(f"Nome: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Situação: {aluno['situacao']}")

aluno = dados_aluno()
mostrar_dados_aluno(aluno)
