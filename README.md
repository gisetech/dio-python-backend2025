# 🏦 Sistema Bancário em Python — Versão 2 (Modularizada)

Este projeto é uma evolução de um sistema bancário simples desenvolvido em Python com instruções do Bootcamp da DIO de Backend Python. A versão 2 traz **modularização com funções**, **cadastro de usuários com validação de CPF e data de nascimento**, e **sistema de contas correntes vinculadas a clientes**.

---

## Funcionalidades

| Função         | Descrição                                                  |
|----------------|------------------------------------------------------------|
| `depositar()`  | Realiza depósitos apenas com argumentos posicionais        |
| `sacar()`      | Realiza saques com argumentos nomeados (keyword only)      |
| `exibir_extrato()` | Exibe extrato com combinação de argumentos posicionais e nomeados |
| `criar_usuario()` | Cadastra novos clientes com validação automática de **CPF e data de nascimento (>=18 anos)**                                              |
| `criar_conta()` | Cria contas vinculado a um usuário existente (`agência fixa 0001`) |
| `listar_contas()` | Lista todas as contas cadastradas                       |



## Regras de Negócio

### Depósitos e Saques

- **Depósito**: Somente valores positivos.
- **Saque**:
  - Máximo de **3 saques por dia**.
  - Limite de saque: **R$ 500 por operação**.
  - Impede saque com saldo insuficiente.

---

### Usuários

Cada usuário possui:


| Campo    | Formato                                             |
|----------|-----------------------------------------------------|
| Nome     | Texto livre                                         |
| CPF      | Armazenado apenas com números (validado)            |
| Nasc     | `dd/mm/aaaa` ou `dd/mm/aa` (>=18 anos)              |
| Endereço | `logradouro, nro - bairro - cidade/UF`              |

⚠️ **Não é permitido cadastrar dois usuários com o mesmo CPF.**

---

### Contas

| Campo | Valor                               |
|--------|------------------------------------|
| Agência | `0001` (fixa)                     |
| Número da Conta | Sequencial (1, 2, 3, ...) |
| Usuário | Associado pelo CPF                |

✔ Um usuário pode possuir **várias contas**, mas **cada conta pertence a apenas um usuário**.

---

## Como Executar

```
python nome_do_arquivo.py
```