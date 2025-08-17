import cliente as cl
from datetime import datetime

def gerenciador_clientes():
    while True:
        print('=' * 30)
        print(' Gerenciador de Clientes '.center(30))
        print('=' * 30)

        print('[1] - Listar Clientes')
        print('[2] - Cadastrar Cliente')
        print('[3] - Atualizar Cliente')
        print('[4] - Desativar Cliente')
        print('[5] - Voltar')

        print('=' * 30)

        opcao = input('-> ')

        if opcao == '1':
            clientes = cl.buscar_clientes()

            print('Clientes:')
            for cliente in clientes:
                print(f'[{cliente.id}] - {cliente.nome}')

        elif opcao == '2':
            nome = input('Digite o nome do cliente: ')
            email = input('Digite o email do cliente: ')
            data_nascimento = input('Digite a data de nascimento do cliente (YYYY-MM-DD): ')
            data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()

            cliente = cl.buscar_cliente_pelo_email(email)

            if cliente is None:
                cliente = cl.Cliente(nome, email, data_nascimento)
                cliente = cl.criar_cliente(cliente)
                print('Cliente cadastrado com sucesso.')
            else: 
                print('Já existe um cliente com esse email.')

        elif opcao == '3':
            # Atualizar Cliente
            cliente_id = input('Digite o ID do cliente a ser atualizado: ')
            
            # Buscando o cliente pelo ID
            cliente = cl.buscar_cliente_por_id(cliente_id)
            
            if cliente:
                print(f"Cliente encontrado: {cliente.nome}")
                
                # Solicitar novos dados
                nome = input(f'Digite o novo nome do cliente (atual: {cliente.nome}): ')
                email = input(f'Digite o novo email do cliente (atual: {cliente.email}): ')
                data_nascimento = input(f'Digite a nova data de nascimento do cliente (atual: {cliente.data_nascimento}): ')
                data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()

                # Atualizar cliente
                cliente.nome = nome
                cliente.email = email
                cliente.data_nascimento = data_nascimento

                cl.atualizar_cliente(cliente)
                print('Cliente atualizado com sucesso.')
            else:
                print('Cliente não encontrado.')

        elif opcao == '4':
            # Desativar Cliente
            cliente_id = input('Digite o ID do cliente a ser desativado: ')
            
            # Buscar cliente pelo ID
            cliente = cl.buscar_cliente_por_id(cliente_id)
            
            if cliente:
                if cliente.fl_ativo:
                    # Desativando cliente
                    cliente.fl_ativo = False
                    cl.atualizar_cliente(cliente)
                    print(f'Cliente {cliente.nome} desativado com sucesso.')
                else:
                    print(f'Cliente {cliente.nome} já está desativado.')
            else:
                print('Cliente não encontrado.')

        elif opcao == '5':
            print('Voltando para a pagina inicial...')
            break

        else:
            print('Opção Inválida')

# Programa Principal
while True:
    print('=' * 30)
    print(' Gerenciador da Loja '.center(30))
    print('=' * 30)

    print('[1] - Gerenciar Clientes')
    print('[2] - Gerenciar Produtos')
    print('[3] - Gerenciar Vendas')
    print('[4] - Sair')

    print('=' * 30)

    opcao = input('-> ')

    if opcao == '1':
        gerenciador_clientes()
    elif opcao == '2':
        pass  # Menu de Produtos
    elif opcao == '3':
        pass  # Menu de Vendas
    elif opcao == '4':
        break
    else:
        print('Opção Inválida')

print('Fim do Programa.')
