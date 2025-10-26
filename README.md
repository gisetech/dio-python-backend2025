# 🏦 Sistema Bancário em Python — Bootcamp DIO Backend Python

Este projeto apresenta a evolução de um sistema bancário desenvolvido em Python durante o Bootcamp da DIO de Backend Python. O repositório contém duas versões do sistema, cada uma explorando diferentes paradigmas e técnicas de programação.

---

## 📂 Estrutura do Projeto

```
sistema-bancario/
│
├── versao_1_funcional.py    # Versão modularizada com funções
└── versao_2_oop.py           # Versão orientada a objetos com classes abstratas
```

---

## 🔄 Versão 1: Programação Funcional Modularizada

Primeira evolução do sistema com **modularização através de funções**, **cadastro de usuários** com validação e **sistema de contas correntes**.

### Funcionalidades

| Função              | Descrição                                                           |
|---------------------|---------------------------------------------------------------------|
| `depositar()`       | Realiza depósitos apenas com argumentos posicionais                 |
| `sacar()`           | Realiza saques com argumentos nomeados (keyword only)               |
| `exibir_extrato()`  | Exibe extrato com combinação de argumentos posicionais e nomeados   |
| `criar_usuario()`   | Cadastra novos clientes com validação de CPF                        |
| `criar_conta()`     | Cria contas vinculadas a um usuário existente (agência fixa 0001)   |
| `listar_contas()`   | Lista todas as contas cadastradas                                   |

### Regras de Negócio

#### Depósitos e Saques

- **Depósito**: Somente valores positivos
- **Saque**:
  - Máximo de **3 saques por dia**
  - Limite de saque: **R$ 500 por operação**
  - Impede saque com saldo insuficiente

#### Usuários

| Campo     | Formato                                    |
|-----------|--------------------------------------------|
| Nome      | Texto livre                                |
| CPF       | Somente números (validado)                 |
| Nascimento| `dd-mm-aaaa`                               |
| Endereço  | `logradouro, nro - bairro - cidade/UF`     |

⚠️ **Não é permitido cadastrar dois usuários com o mesmo CPF.**

#### Contas

| Campo           | Valor                      |
|-----------------|----------------------------|
| Agência         | `0001` (fixa)              |
| Número da Conta | Sequencial (1, 2, 3, ...)  |
| Usuário         | Associado pelo CPF         |

✔ Um usuário pode possuir **várias contas**, mas **cada conta pertence a apenas um usuário**.

---

## 🎯 Versão 2: Programação Orientada a Objetos (OOP)

Segunda versão do sistema implementando **orientação a objetos**, **classes abstratas**, **herança** e **encapsulamento**.

### Arquitetura de Classes

```
Cliente (classe base)
└── PessoaFisica

Conta (classe base)
└── ContaCorrente

Transacao (classe abstrata - ABC)
├── Deposito
└── Saque

Historico (classe de suporte)
```

### Principais Conceitos OOP Implementados

- ✅ **Classes Abstratas (ABC)**: `Transacao` define interface para operações
- ✅ **Herança**: `PessoaFisica` herda de `Cliente`, `ContaCorrente` herda de `Conta`
- ✅ **Encapsulamento**: Atributos privados com properties para acesso controlado
- ✅ **Polimorfismo**: Métodos `registrar()` implementados de forma diferente em `Saque` e `Deposito`
- ✅ **Composição**: `Cliente` possui `Conta`, `Conta` possui `Historico`

### Classes e Responsabilidades

| Classe          | Responsabilidade                                    |
|-----------------|-----------------------------------------------------|
| `Cliente`       | Gerenciar dados e contas do cliente                 |
| `PessoaFisica`  | Especialização de Cliente com CPF e dados pessoais  |
| `Conta`         | Gerenciar saldo e operações bancárias básicas       |
| `ContaCorrente` | Conta com limite de saque e quantidade de saques    |
| `Historico`     | Armazenar histórico de transações com data/hora     |
| `Transacao`     | Classe abstrata base para operações bancárias       |
| `Saque`         | Implementação concreta de operação de saque         |
| `Deposito`      | Implementação concreta de operação de depósito      |

### Funcionalidades Adicionais (Versão OOP)

- 📅 **Histórico com Data/Hora**: Cada transação registra timestamp
- 🔒 **Encapsulamento**: Saldo e dados sensíveis protegidos
- 🏗️ **Factory Method**: Método `nova_conta()` para criação de contas
- 📊 **Extrato Detalhado**: Mostra tipo, valor e data/hora de cada transação

---

## 🚀 Como Executar

### Versão 1 (Funcional)
```bash
python versao_1_funcional.py
```

### Versão 2 (OOP)
```bash
python versao_2_oop.py
```

---

## 📋 Menu de Operações (Versão 2)

```
================ MENU ================
[1]    Depositar
[2]    Sacar
[3]    Extrato
[4]    Nova conta
[5]    Listar contas
[6]    Novo usuário
[0]    Sair
```

### Fluxo de Uso Recomendado

1. **[6]** Criar novo usuário
   - Informe CPF (somente números)
   - Nome completo
   - Data de nascimento (`dd-mm-aaaa`)
   - Endereço completo

2. **[4]** Criar conta para o usuário
   - Informe o CPF do usuário cadastrado

3. **[1]** Fazer depósito
   - Informe CPF e valor

4. **[2]** Realizar saque
   - Informe CPF e valor (limite R$ 500, máx 3 saques)

5. **[3]** Consultar extrato
   - Informe CPF para ver histórico completo

### Exemplo Prático

```
[6] → CPF: 12345678900, Nome: João Silva
[4] → CPF: 12345678900 (cria conta)
[1] → CPF: 12345678900, Valor: 1000
[2] → CPF: 12345678900, Valor: 200
[3] → CPF: 12345678900 (saldo: R$ 800,00)
```

---

## 🎓 Conceitos Aplicados

### Versão 1
- ✅ Funções com argumentos posicionais e nomeados
- ✅ Modularização de código
- ✅ Validação de dados de entrada
- ✅ Estruturas de dados (listas e dicionários)

### Versão 2
- ✅ Programação Orientada a Objetos
- ✅ Classes Abstratas (ABC)
- ✅ Herança e Polimorfismo
- ✅ Encapsulamento e Properties
- ✅ Composição de objetos
- ✅ Design Patterns (Factory Method)
- ✅ SOLID Principles (Single Responsibility, Open/Closed)

---

## 📝 Regras Comuns às Duas Versões

### Limitações de Saque
- Limite por operação: **R$ 500,00**
- Limite diário: **3 saques**
- Saldo deve ser suficiente

### Validações
- CPF único por usuário
- Valores de depósito/saque devem ser positivos
- Conta deve estar vinculada a um usuário existente

---

## 🔧 Tecnologias Utilizadas

- **Python 3.x**
- **Módulos**: `textwrap`, `abc` (Abstract Base Classes), `datetime`

---


## 👨‍💻 Autor

Desenvolvido durante o Bootcamp Backend Python da DIO

---

## 📄 Licença

Este projeto é livre para uso educacional.
