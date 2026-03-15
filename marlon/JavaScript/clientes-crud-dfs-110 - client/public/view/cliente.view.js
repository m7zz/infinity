export const clienteForm = document.getElementById("cliente-form");
const clientesTable = document.getElementById("clientes-table");

export function adicionarClienteTabela(cliente) {
  const tableData = clientesTable.querySelector("tbody");

  const tableRow = document.createElement("tr");
  tableData.appendChild(tableRow);

  const nomeCell = document.createElement("td");
  nomeCell.innerText = cliente.nome;
  tableRow.appendChild(nomeCell);

  const emailCell = document.createElement("td");
  emailCell.innerText = cliente.email;
  tableRow.appendChild(emailCell);

  const telCell = document.createElement("td");
  telCell.innerText = cliente.endereco;
  tableRow.appendChild(telCell);

}

export function mostrarMensagem(text, type) {
  const mensagemParagraph = document.getElementById("mensagem");

  mensagemParagraph.innerText = text;
  mensagemParagraph.style.fontWeight = "bold";
  mensagemParagraph.style.color = type == "success" ? "green" : "red";
}