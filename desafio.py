menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        print(numero_saques)
        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número de saques esgotados.")
        else:
            valor = float(input("Informe o valor a ser sacado: "))
            if valor <= 0:
                print("Operação falhou! O valor informado é inválido.")
            elif valor > saldo:
                print("Operação falhou! Saldo insuficiente.")
            elif valor > limite:
                print("Operação falhou! O valor informado excede o limite de R$ 500.00 que pode ser sacado.")
            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso.")

    elif opcao == "e":
        print("EXTRATO".center(40, "#"))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("".center(40, "#"))
       
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

