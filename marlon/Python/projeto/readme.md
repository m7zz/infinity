# Projeto - Gerenciador de Vendas

Você foi contratado para criar um software de gerenciamento de vendas, que será utilizado por um operador. O software deverá ter 3 módulos:

1. Modulo de Gerenciamento de Clientes
2. Modulo de Gerenciamento de Produtos
3. Modulo de Gerenciamento de Vendas


## Gerenciamento de Clientes

Os dados do cliente deverão ser armazenados em uma tabela (SQL) onde deverá ser obrigatório solicitar nome, email e data_nascimento do cliente.

```sql
CREATE TABLE clientes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    fl_ativo BOOL NOT NULL DEFAULT true
)
```

Este modulo deve possibilitar:

- Listar Clientes
- Cadastrar Clientes
- Atualizar Clientes
- Desativar Clientes

## Gerenciamento de Produtos

Os dados dos produtos deverão ser armazenados em uma tabela (SQL) onde deverá solicitar nome, preco, descricao (Opcional) e quantidade do produto.

```sql
CREATE TABLE produtos (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    preco DECIMAL(6, 2) NOT NULL,
    descricao VARCHAR(500),
    quantidade INTEGER NOT NULL DEFAULT 0
)
```

Este modulo deve possibilitar:

- Listar Produtos
- Cadastrar Produtos
- Atualizar Produtos

## Gerenciamento de Vendas

As vendas deverão ser registradas em uma tabela (SQL), onde no fluxo de cadastrar uma venda deve ser solicitado:

- O id do cliente (Não listar clientes inativos)
- O id do produto (Não listar produtos com quantidade = 0)
- Quantidade que o cliente está comprando

```sql
CREATE TABLE vendas (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	produto_id INTEGER NOT NULL,
    cliente_id INTEGER NOT NULL,
	quantidade INTEGER NOT NULL,
	preco_referencia DECIMAL(6, 2) NOT NULL,
	data_hora DATETIME NOT NULL,
	total DECIMAL(6, 2) NOT NULL,
	FOREIGN KEY produto_id REFERENCES produtos(id)
	FOREIGN KEY cliente_id REFERENCES clientes(id)
)
```

O modulo de vendas deve possibilitar:

- Listar Vendas
- Cadastrar Vendas
- Excluir Vendas

-