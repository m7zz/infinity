
numeros = []
while True:
   
    try:
        numero = float(input("Digite um número: "))
        numeros.append(numero)
        
        continuar = input("Deseja continuar? [S/N]: ").upper()
       
        if continuar != 'S':
            break
            
    except ValueError:
        print("Por favor, digite um número válido!")
        continue

if len(numeros) > 0:
    
    quantidade = len(numeros)
    menor = min(numeros)
    maior = max(numeros)
    soma = sum(numeros)
    media = soma / quantidade
    
    print("\nResultados:")
    print(f"Quantidade de números inseridos: {quantidade}")
    print(f"Menor número: {menor}")
    print(f"Maior número: {maior}")
    print(f"Soma dos números: {soma}")
    print(f"Média dos números: {media:.2f}")
else:
    print("\nNenhum número foi inserido!")