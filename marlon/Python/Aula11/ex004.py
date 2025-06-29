class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def adicao(self):
        return self.num1 + self.num2
    def subtracao(self):
        return self.num1 - self.num2
    def multiplicar(self):
        return self.num1 * self.num2
    def dividir(self):
        return self.num1 / self.num2