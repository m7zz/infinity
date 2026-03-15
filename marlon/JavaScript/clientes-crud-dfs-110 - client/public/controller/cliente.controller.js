import { adicionarClienteTabela, clienteForm, mostrarMensagem } from "../view/cliente.view.js";
import { salvarCliente, buscarClientes } from "../model/cliente.model.js";

clienteForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const cliente = {
    nome: clienteForm.nome.value.trim(),
    email: clienteForm.email.value.trim(),
    endereco: clienteForm.endereco.value.trim(),
  };

  if (cliente.nome === "") {
    mostrarMensagem("O campo nome é obrigatório.", "error");
    return;
  }

  if (cliente.email === "") {
    mostrarMensagem("O campo email é obrigatório.", "error");
    return;
  }

  if (cliente.endereco === "") {
    mostrarMensagem("O campo endereço é obrigatório.", "error");
    return;
  }

  salvarCliente(cliente);
  adicionarClienteTabela(cliente);
  mostrarMensagem("Cliente cadastrado com sucesso.", "success");

  clienteForm.reset();
});

async function handleListarClientes(params) {
    const clientes = await buscarClientes();
    clientes.forEach((cliente) => adicionarClienteTabela(cliente));
}


document.addEventListener("DOMContentLoaded", handleListarClientes);
