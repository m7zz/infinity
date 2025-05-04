"""Ex04
a) Faça uma função chamada "calcular_imc" que recebe o peso e a altura e retorna o valor do IMC
Formula: peso / altura ** 2

b) Faça uma função chamada "classificar_imc" que recebe o valor do IMC e retorna uma STRING com a classificacao de acordo com a tabela IMC:

- 'ABAIXO_DO_PESO' se estiver menor ou igual a 18.5
- 'PESO_IDEAL' se estiver entre 18.5 e 25 (final incluso)
- 'SOBREPESO' se estiver entre 25 e 30 (final incluso)
- 'OBESIDADE_I' se estiver entre 30 e 35 (final incluso)
- 'OBESIDADE_II' se estiver entre 35 e 40 (final incluso)
- 'OBESIDADE_III' se for maior que 40"""

def calcular_imc(peso, altura):
    return peso / altura ** 2

peso = float(input("Digite seu peso em KG:"))
altura = float(input("Digite sua altura em metros: "))

def classificar_imc(imc):
    if imc <= 18.5:
        return 'Abaixo_do_Peso!'
    elif imc <= 25:
        return 'Peso_Ideal'
    elif imc <= 30:
        return "Sobre_Peso"
    elif imc <= 35:
        return "Obesidade_1"
    elif imc <= 40:
        return "Obesidade_2"
    else:
        return "Obesidade_3"
    
imc = calcular_imc(peso,altura)

classificacao = classificar_imc(imc)

print(f'O seu IMC é {imc:.2f}')
print(f'A classificacao do seu imc é {classificacao}')