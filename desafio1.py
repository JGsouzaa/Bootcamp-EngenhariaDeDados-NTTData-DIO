saldo = 700
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """\n
================ MENU ================
d  - Depositar
s  - Sacar
e  - Extrato
nc - Nova conta
lc - Listar contas
nu - Novo usuário
q  - Sair
=> """

while True:

    selecao = input(menu)

    if selecao == "s":
        valor = float(input("Informe o valor do saque: "))

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
            print("Extrato de operação: ", extrato)
        else:
            print("O valor informado é inválido.")
    elif selecao == "d":
        valor = float(input("Informe o valor de deposito: "))
             
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Extrato de operação: ", extrato)
        else:
            print("O valor informado é inválido.")



