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
  RELATÓRIO DE DESENVOLVIMENTO - CONTROLE DE ESTOQUE
Data: 20/08/2025 14:48

Resumo das atividades de hoje:

Ativação do Banco de dados:
   - Uso do SQLite3 para armazenar produtos (estoque.db).
   - Criação da tabela de produtos (id, nome, quantidade).
   - Testes no terminal para verificar se os dados estão sendo salvos.

 Problemas encontrados:
   - Dificuldade em abrir e visualizar o estoque.db diretamente.
   - Necessidade de criar script auxiliar (teste_bd.py) para verificar dados no banco.
   - Execução do script retornou vazio (indicando que não havia dados ou que ainda não estava funcionando corretamente).
   - Corrigido erro de digitação ao rodar comandos no terminal interativo.

 Próximos passos sugeridos:
   - Verificar se o formulário HTML está enviando os dados corretamente para o backend.
   - Garantir que a função de inserção no banco de dados esteja funcionando (inserir e listar produtos).
   - Criar botões visuais para "Adicionar" e "Excluir" sem uso de emojis.
   - Melhorar o feedback visual na página (mensagens de confirmação).

Arquivos criados/alterados hoje:
- app.py (lógica principal do Flask)
- templates/index.html (listagem de produtos)
- templates/add.html (formulário para adicionar produtos)
- teste_bd.py (script auxiliar para verificar dados do banco)

Observações finais:
O projeto avançou de um simples script em Python para uma aplicação web com Flask e banco SQLite. 
Ainda é necessário ajustar a exibição dos dados na página, mas já temos a estrutura principal em funcionamento.

