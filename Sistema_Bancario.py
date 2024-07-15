def menu():
    menu = '''\n  
    ====== MENU ======
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas
    [6] Novo Usuário
    [0] Sair
    ==================
    Digite uma opção: '''
    return input(menu)

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso!")
    else:
        print("\n Falha! O valor informado é inválido.")

    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor >limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n Falha! Você não tem saldo suficiente.")
    
    elif excedeu_limite:
        print(f"\n Falha! O valor do saque excede o limite de R$ {limite:.2f}")
    
    elif excedeu_saques:
        limite_saques = 3
        print(f"\n Falha! Número de saques excedido. Você pode fazer {limite_saques} por dia.")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso!")
    
    else:
        print("\n Falha! O valor informado é inválido!")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n ====== EXTRATO ======")
    if saldo == 0:
        print("\n Não há movimento na sua conta!")
    elif saldo > 0:
        linhas_extrato = extrato.strip().split('\n')
        for i, linha in enumerate(linhas_extrato, start=1):
            print(f"#{i} {linha}")
        print(f"\n Saldo atual: R$ {saldo:.2f}")
    print("\n =====================")

def criar_usuario(usuarios):
    cpf = input("\n Informe seu CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n Já existe usuário com esse CPF!")
        return
    
    nome = input(" Informe seu nome completo: ")
    data_nascimento = input(" Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input(" Informe seu endereço (logradouro, nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("\n Informe seu CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(" Conta criada com sucesso!\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print(" Usuário não encontrado! Fluxo de criação de conta encerrado.\n")
    
def listar_contas(contas):
    if contas:
        for conta in contas:
            informacoes_usuario = f'''
            \n\tAgência: {conta['agencia']}
            \n\tC/C:     {conta['numero_conta']} 
            \n\tTitular: {conta['usuario']['nome']}'''
            
            print("\n\t")
            print("=" * 50)
            print(informacoes_usuario)
        return
    print("\n Nenhuma conta cadastrada!")
    

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True: 

        opcao = menu()

        if opcao == "1":
            valor_deposito = float(input("\n Digite o valor que você quer depositar: "))
            saldo, extrato = deposito(saldo, valor_deposito, extrato)
    
        elif opcao == "2":
            valor_saque = float(input("\n Digite o valor que você quer sacar: "))
            saldo, extrato = saque(
                saldo=saldo, 
                valor=valor_saque, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES,
            )
            
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            numero_contas = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_contas, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)     
    
        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "0": 
            break

        else:
            print(" Operação inválida, por favor selecione novamente a operação desejada.")

main()