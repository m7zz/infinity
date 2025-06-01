def apresentar(*args):
    for pessoa in args:
        print(f"Olá, meu nome é {pessoa}!")

# Chamadas com diferentes quantidades de argumentos
apresentar("Lucas", "Ana", "Carlos")
apresentar("Rita")
