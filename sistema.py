# Variáveis globais
AGENCIA = "0001"
VALOR_LIMITE_POR_SAQUE = 5000
LIMITE_SAQUES_DIARIOS = 3

saques = 0

saldo = 0
qntde_de_depositos = 0
usuarios = []
contas = []




# Funções
def depositar(saldo, qntde_de_depositos):
    valor = float(input("Digite o valor que você quer depositar: "))
    if valor <= 0:
        print("O depósito deve ser de no mínimo R$ 1.00")
    else:
        print("Depósito realizado!")
        saldo += valor
        qntde_de_depositos += 1
    print(f"Seu saldo atual é de R$ {saldo:.2f}")
    return saldo, qntde_de_depositos

def sacar(saldo, saques, LIMITE_SAQUES_DIARIOS):
    valor = float(input("Qual valor você quer sacar: "))
    if valor > VALOR_LIMITE_POR_SAQUE:
        print(f"Você só pode sacar R$ {VALOR_LIMITE_POR_SAQUE} por vez.")
    elif saques >= LIMITE_SAQUES_DIARIOS:
        print("Você atingiu o limite de saques diários.")
    elif valor > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= valor
        saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo, saques

def mostrar_extrato(saques, qntde_de_depositos, saldo):
    print(f"""
    ============== EXTRATO ==============
    Saques hoje: {saques}
    Depósitos hoje: {qntde_de_depositos}
    Saldo atual: R$ {saldo:.2f}
    =====================================
    """)

def consultar_saldo(saldo):
    print(f"Seu saldo atual é de R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF (somente números): ").strip()
    
    # Verifica se CPF já existe
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Usuário já existe!")
            return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, número - bairro - cidade/estado): ")

    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "nascimento": nascimento,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")

def criar_conta(AGENCIA, contas, usuarios):
    cpf = input("Digite o CPF do titular da conta: ").strip()

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        numero_conta = len(contas) + 1
        contas.append({
            "agencia": AGENCIA,
            "numero_conta": numero_conta,
            "usuario": usuario_encontrado
        })
        print(f"Conta criada com sucesso! Agência: {AGENCIA} Conta: {numero_conta}")
    else:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        print(f"""
        Agência: {conta['agencia']}
        Número da Conta: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        CPF: {conta['usuario']['cpf']}
        """)


# Menu
menu = """
    [0] Sair
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Consultar saldo
    [5] Criar novo usuário
    [6] Nova conta
    [7] Listar contas
"""

# Loop principal
while True:
    print(menu)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        print("Obrigado por utilizar nosso sistema!")
        break

    elif opcao == 1:
        saldo, qntde_de_depositos = depositar(saldo, qntde_de_depositos)

    elif opcao == 2:
        saldo, saques = sacar(saldo, saques, LIMITE_SAQUES_DIARIOS)
    elif opcao == 3:
        mostrar_extrato(saques, qntde_de_depositos, saldo)

    elif opcao == 4:
        consultar_saldo(saldo)
    
    elif opcao == 5:
        criar_usuario(usuarios)

    elif opcao == 6:
        criar_conta(AGENCIA, contas, usuarios)

    elif opcao == 7:
        listar_contas(contas)

    else:
        print("Opção invalida!!!!")
