LIMITE_SAQUES = 3
AGENCIA = "1000"
saldo = 700
limite = 500
numero_saques = 0
extrato = ""
contas = []
usuarios = []

menu = """\n
================ MENU ================
s  - Sacar
d  - Depositar
e  - Extrato
nc - Nova conta
lc - Listar contas
nu - Novo usuário
q  - Sair
=> """

def extrato_operacao(extrato):
    print("Extrato de operação: ", extrato)

def saque(*, saldo, valor, extrato, limite, numero_saque, limite_saques):
    if valor > saldo:
        print("Você não tem saldo suficiente.")
    elif limite < valor:
        print("O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        extrato_operacao(extrato)
    else:
        print("O valor informado é inválido.")

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        extrato_operacao(extrato)
    else:
        print("O valor informado é inválido.")

    return(saldo, extrato)

def exibe_extrato(saldo, extrato = extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def nova_conta(agencia, numero_agencia, usuarios):
    cpf = input("Informe o CPF (apenas números) do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, erro durante criação de conta!")

def listar_contas(contas):
    for conta in contas:
        print(f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """)

def novo_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nCPF já cadastrado!")
        return

    nome = input("Informe o nome completo: ")
    endereco = input("Informe o endereço (logradouro, número - bairro - cidade e estado): ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return(usuarios_filtrados[0] if usuarios_filtrados else None)

while True:

    selecao = input(menu)

    if selecao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = saque(saldo = saldo, valor = valor, extrato = extrato,
                                 limite = limite, numero_saques = numero_saques, 
                                 limite_saques = LIMITE_SAQUES)

    elif selecao == "d":
        valor = float(input("Informe o valor de deposito: "))

        saldo, extrato = deposito(saldo, valor, extrato)

    elif selecao == "e":
        exibe_extrato(saldo, extrato = extrato)
    
    elif selecao == "nc":
        numero_conta = len(contas) + 1
        conta = nova_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif selecao == "lc":
        listar_contas(contas)

    elif selecao == "nu":
        novo_usuario(usuarios)

    elif selecao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")