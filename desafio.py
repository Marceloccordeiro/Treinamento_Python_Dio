def menu_principal():
    return """\n====== MENU PRINCIPAL ======
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n✅ Depósito realizado com sucesso!")
    else:
        print("\n❌ Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    if valor <= 0:
        print("\n❌ Operação falhou! O valor informado é inválido.")
    elif valor > saldo:
        print("\n❌ Saldo insuficiente para essa operação.")
    elif valor > limite:
        print("\n❌ Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("\n❌ Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n✅ Saque realizado com sucesso!")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# ======== VARIÁVEIS INICIAIS ========
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# ======== LOOP PRINCIPAL ========
while True:
    opcao = input(menu_principal()).lower()

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "q":
        print("\n👋 Obrigado por usar nosso sistema. Volte sempre!")
        break

    else:
        print("\n❌ Operação inválida! Escolha uma opção válida.")
