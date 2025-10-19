from datetime import datetime

# ----------------- VALIDADORES -----------------

def validar_cpf(cpf: str) -> bool:
    """
    Remove tudo que não é dígito e valida o CPF com o algoritmo oficial.
    Retorna True se válido, False caso contrário.
    """
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    # Validação dos dois dígitos verificadores
    for i in range(9, 11):
        soma = 0
        for num in range(0, i):
            soma += int(cpf[num]) * ((i + 1) - num)
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(cpf[i]):
            return False

    return True


def validar_data_nascimento(data: str) -> bool:
    """
    Verifica se a data está no formato dd/mm/aaaa ou dd/mm/aa e se o usuário tem >= 18 anos.
    Retorna True se válido, False caso contrário.
    """
    try:
        # Tenta primeiro com ano completo (aaaa)
        nascimento = datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        try:
            # Se falhar, tenta com ano abreviado (aa)
            nascimento = datetime.strptime(data, "%d/%m/%y")
        except ValueError:
            return False
    
    hoje = datetime.today()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade >= 18


# ----------------- FUNÇÕES DO SISTEMA -----------------

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("❌ Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("❌ Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("❌ Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("✅ Saque realizado com sucesso!")
    else:
        print("❌ Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("✅ Depósito realizado com sucesso!")
    else:
        print("❌ Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


# ----------------- USUÁRIOS E CONTAS -----------------

def filtrar_usuario(cpf, usuarios):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)


def criar_usuario(usuarios):
    cpf_input = input("Informe o CPF (somente números ou com separadores): ").strip()
    cpf = ''.join(filter(str.isdigit, cpf_input))

    if not validar_cpf(cpf):
        print("❌ CPF inválido! Cadastro cancelado.")
        return

    if filtrar_usuario(cpf, usuarios):
        print("❌ Já existe usuário com esse CPF!")
        return

    nome = input("Nome completo: ").strip()
    nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()

    if not validar_data_nascimento(nascimento):
        print("❌ Data inválida ou menor de 18 anos! Cadastro cancelado.")
        return

    endereco = input("Endereço (logradouro, nro - bairro - cidade/UF): ").strip()

    usuarios.append({
        "nome": nome,
        "data_nascimento": nascimento,
        "cpf": cpf,  # armazenamos somente números
        "endereco": endereco
    })

    print("✅ Usuário criado com sucesso!")


def criar_conta(agencia, numero_conta, usuarios):
    cpf_input = input("Informe o CPF do titular (somente números ou com separadores): ").strip()
    cpf = ''.join(filter(str.isdigit, cpf_input))

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("✅ Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("❌ Usuário não encontrado! Criação de conta encerrada.")
    return None


def listar_contas(contas):
    print("\n====== LISTA DE CONTAS ======")
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta in contas:
            print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']} | CPF: {conta['usuario']['cpf']}")
    print("=============================\n")


# ----------------- PROGRAMA PRINCIPAL -----------------

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0.0
    limite = 500.0
    extrato = ""
    numero_saques = 0

    usuarios = []
    contas = []

    menu = """
====== MENU ======
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta
[6] Listar Contas
[7] Sair
==================
=> """

    while True:
        opcao = input(menu).strip()

        if opcao == "1":
            try:
                valor = float(input("Informe o valor do depósito: "))
            except ValueError:
                print("❌ Valor inválido.")
                continue
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            try:
                valor = float(input("Informe o valor do saque: "))
            except ValueError:
                print("❌ Valor inválido.")
                continue
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "3":
            exibir_extrato(saldo, extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            print("✅ Saindo do sistema...")
            break

        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()
