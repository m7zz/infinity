# class Cachorro:
#     def __init__(self,nome, altura, peso,raca ):
#         self.nome = nome
#         self.altura = altura
#         self.peso = peso
#         self.raca = raca
# cachorro1 = Cachorro('AteroidDestroyer', 5, 200, 'Boxer')class Carro:















class Carro:
    def __init__(self,marca, modelo, ano): 
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    def __str__(self):
        return f'O {self.modelo} é da marca {self.marca} e é do ano {self.ano}'

    def ligar(self):
        return f'O carro {self.modelo} esta ligado'



carro1 = Carro('Lamborguini', 'Huracan', 2027)
carro2 = Carro('Ferrari', 'Roma', 2020 )

