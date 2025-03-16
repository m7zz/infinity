"""Ex03. Faça um programa que peça 5 numeros para o usuário
e mostre o maior numero inserido."""

maior = int(input("Digite o primeiro número: "))  # Inicializa com o primeiro número

for i in range(1, 5):  # Começa de 1 porque já pegamos o primeiro número
    numero = int(input(f"Digite o número {i+1}: "))
    
    if numero > maior:
        maior = numero

# Exibe o maior número
print(f'O maior número é {maior}')
