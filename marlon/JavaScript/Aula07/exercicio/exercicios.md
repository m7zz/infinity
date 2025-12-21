# Exercicios

## Ex01.

Faça um programa em javascript que mostre um "Olá Mundo" e execute com o node js.

## Ex02.

Faça um programa em javascript, crie um array com o nome de 5 cidades e mostre:

- A primeira cidade.
- A cidade no indice 3 (Qual é a posição dessa cidade?).
- A ultima cidade.

## Ex03.

Faça um programa que tenha um array de 6 numeros, e utilize o "for" ou o "forEach" para mostrar todos os numeros.

## Ex04.

Faça um programa que deve conter um input e um botão no HTML. Quando o usuário digitar um nome, e clicar em "Adicionar" você deve adicionar esse nome em uma lista de "nomes" e mostrar a lista na tela.

Pode utilizar o HTML abaixo como referência:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Lista de Nomes</title>
  </head>
  <body>
    <h1>Nomes</h1>

    <div>
      <input type="text" id="nome" placeholder="Digite um nome" />
      <button onclick="handleAdicionarNome()">Adicionar</button>
    </div>

    <ul id="nomes"></ul>

    <script>
      const nomes = [];

      function handleAdicionarNome() {
        // 1. Buscar o valor do Input "nome"
        
        // 2. Adicionar o Nome na Lista

        // 3. Chamar a função "handleMostrarNomes"
      }

      function handleMostrarNomes() {
        // 1. Buscar a Lista (ul) no HTML e armazenar em uma variavel

        // 2. Limpar variavel da ul de nomes

        // 3. Percorrer o array de nomes, e para cada nome, adicionar um <li>
      }
    </script>
  </body>
</html>