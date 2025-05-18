def imprimir_info(nome, *args):
    print(f"Nome: {nome}")
    print("Outras informações:")
    for info in args:
        print(info)

# Chamando a função
imprimir_info("João", "27 anos", "Programador", "Gosta de videogames")
