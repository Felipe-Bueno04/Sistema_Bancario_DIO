menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

Digite uma opção: '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("\nDepósito")
        valor_deposito = float(input("Digite o valor que você quer depositar: "))
        saldo += valor_deposito
        extrato += f"Depósito de R$ {valor_deposito:.2f}\n"
    
    elif opcao == "2":
        print("\nSaque")
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor que você quer sacar: "))
            if saldo == 0:
                print("Você não pode sacar, não há saldo na conta!")
            if valor_saque > saldo:
                print("Saldo insuficiente!") 
            elif valor_saque > limite:
                print(f"Seu limite máximo de saque é R$ {limite:.2f}!")
            elif valor_saque > 0:
                saldo -= valor_saque
                extrato += f"Saque de R$ {valor_saque:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
        else:
            print("Limite diário de saques atingido.")
            
    elif opcao == "3":
        print("\nExtrato")
        if saldo == 0:
            print("Não há movimento na sua conta!")
        elif saldo > 0:
            linhas_extrato = extrato.strip().split('\n')
            for i, linha in enumerate(linhas_extrato, start=1):
                print(f"#{i} {linha}")
            print(f"\nSaldo atual: R$ {saldo:.2f}")
    
    elif opcao == "0": 
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
