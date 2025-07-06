# Heranca

class Conta:
    def __init__(self, titular: str, numero: str, saldo: float = 0):
        self.titular = titular
        self.numero = numero

        if saldo < 0:
            raise ValueError('O saldo inicial deve ser maior ou igual a 0')

        self.saldo = saldo

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de depósito deve ser maior que 0')
        
        self.saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de saque deve ser maior que 0')
        
        if valor > self.saldo:
            raise ValueError('Saldo insuficiente.')
        
        self.saldo -= valor

    def transferir(self, valor: float, conta_destino: 'Conta'):
        self.sacar(valor)
        conta_destino.depositar(valor)

    def __str__(self):
        return f'{self.titular} (Nº{self.numero}) - R${self.saldo:.2f}'
    
    