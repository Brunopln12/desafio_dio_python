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
        saldo_insuficiente = saldo == 0
        if saldo_insuficiente:
            print("Operação falhou! Sem saldo em sua conta.")
            break

        if LIMITE_SAQUES == numero_saques:
            valor = float(input("Informe o valor a ser sacado: "))
            valor_sacado_maior_que_saldo_em_conta = valor < saldo
            pode_sacar = valor < 500
            if pode_sacar:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Operação falhou! O valor informado é inválido.")
        else:
            print("Operação falhou! Número de saques esgotados.")
    # elif opcao == "e":
       
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

