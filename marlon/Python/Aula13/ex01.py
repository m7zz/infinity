class Conta:
    def __init__(self, titular: str, numero: str, saldo: float = 0.0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo if saldo >= 0 else 0.0

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor de depósito deve ser positivo.")
        self.saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor de saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente, você não tem dinheiro suficiente.")
        self.saldo -= valor

    def transferir(self, valor: float, conta_destino: 'Conta'):
        if valor <= 0:
            raise ValueError("O valor de transferência deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para transferência.")
        self.saldo -= valor
        conta_destino.depositar(valor)


# Criando as contas
conta1 = Conta("João", "12345", 1000)
conta2 = Conta("Maria", "67890", 500)

while True:
    # Menu de opções
    print("\nMenu:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Transferência")
    print("4 - Ver Saldo")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção (1/2/3/4/5): ")

    if opcao == '1':
        try:
            valor = float(input("Digite o valor para depósito: R$"))
            conta1.depositar(valor)
            print(f"Depósito realizado com sucesso! Novo saldo de João: R${conta1.saldo:.2f}")
        except ValueError as e:
            print("Erro:", e)

    elif opcao == '2':
        try:
            valor = float(input("Digite o valor para saque: R$"))
            conta1.sacar(valor)
            print(f"Saque realizado com sucesso! Novo saldo de João: R${conta1.saldo:.2f}")
        except ValueError as e:
            print("Erro:", e)

    elif opcao == '3':
        try:
            valor = float(input("Digite o valor para transferência: R$"))
            conta1.transferir(valor, conta2)
            print(f"Transferência realizada com sucesso! Novo saldo de João: R${conta1.saldo:.2f}")
            print(f"Novo saldo de Maria: R${conta2.saldo:.2f}")
        except ValueError as e:
            print("Erro:", e)

    elif opcao == '4':
        print(f"\nSaldo atual de João: R${conta1.saldo:.2f}")
        print(f"Saldo atual de Maria: R${conta2.saldo:.2f}")

    elif opcao == '5':
        print("Saindo... Obrigado por utilizar o sistema!")
        break  # Sai do loop while e termina o programa

    else:
        print("Opção inválida! Tente novamente.")
