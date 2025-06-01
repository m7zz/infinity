# Faça um algoritimo que receba um nmr e defina se ele é par.

def definePar(num) :
    resultado = ""
    if num % 2 == 0:
        resultado = "O número é par"
    else:
        resultado = "O número é impar"

    return resultado 

print(definePar(5))