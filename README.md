# Controle de Estoque Web

**Data:** 18/08/2025

Este projeto é um **controle de estoque web** simples, desenvolvido em **Python** usando o **Flask** para o backend e **SQLite** como banco de dados.

## O que foi construído até agora

Atualmente, o projeto contém apenas o arquivo principal `app.py`, que implementa a lógica do backend:

- Conexão com o banco de dados SQLite (`estoque.db`)
- Criação automática da tabela `produtos`
- Rotas implementadas:
  - `/` → lista todos os produtos cadastrados
  - `/add` → adiciona novos produtos (nome e quantidade)
  - `/delete/<id>` → remove produtos pelo ID

## Observações

- Ainda não foram criados os arquivos HTML (`index.html` e `add.html`), então a aplicação não possui interface visual e gerará erro ao acessar as rotas no navegador.
- O banco de dados será criado automaticamente ao rodar o `app.py`, não sendo necessário criá-lo manualmente.
- O projeto serve como **base para estudo de Flask, SQLite e lógica de CRUD**.

## Próximos passos

- Criar os arquivos de template HTML (`index.html` e `add.html`) para permitir interação via navegador.
- Adicionar funcionalidades extras como edição de produtos ou validação de formulários.
