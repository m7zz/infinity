# calculadora de divisao

def calculadora():
    while True:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
   
            resultado = numero1 / numero2
            
        except ValueError:
            
            print("Erro: Por favor, insira apenas números válidos!")
            continue
        except ZeroDivisionError:

            print("Erro: Não é possível dividir por zero. Tente novamente.")
            continue
        else:

            print(f"O resultado da divisão é: {resultado}")
            break

calculadora()
