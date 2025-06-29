class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    def __str__(self):
        return f"{self.nome} - {self.cargo} - R${self.salario:.2f}"
    

class Empresa:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, nome, cargo, salario):
        funcionario = Funcionario(nome, cargo, salario)
        self.funcionarios.append(funcionario)
        print(f"{nome} foi adicionado.")
    
    def remover_funcionario(self,nome):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                self.funcionarios.remove(funcionario)
                print(f'{nome} foi removido da empresa.')
                return
        print(f"Funcionário {nome} não encontrado.")
    
    def listar_funcionarios(self):
                if not self.funcionarios:
                     print('Nao há funcionarios.')
                else : 
                      print("Lista de Funcionários:")
                      for funcionario in self.funcionarios:
                           print(funcionario)

def menu():
         empresa = Empresa()

         while True:
              print('\n--- MENU LINDAO ---')
              print('\n 1. Adicionar Funcionario')
              print('\n 2. Remover Funcionario')
              print('\n 3. Listar Funcionarios')
              print('\n 4. Sair \n')
              opcao = input('Escolha uma opção: ')

              if opcao == '1':
                   nome = input('Digite o nome do novo funcionario: ')
                   cargo = input('Digite o cargo que o funcionario ira receber: ')
                   salario = float(input('Digite o salario do funcionario: '))
                   empresa.adicionar_funcionario(nome,cargo,salario)

              elif opcao == '2':
                   nome = input('Digite o nome do funcionario que ira ser removido: ')
                   empresa.remover_funcionario(nome)
              
              elif opcao == '3':
                   empresa.listar_funcionarios()
              
              elif opcao == '4':
                   print('Saindo do sistema.')
                   break
              
              else:
                   print('Opção invalida! tente novamente')


menu()