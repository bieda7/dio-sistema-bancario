menu = """

[0] Sair
[1] Depositar
[2] Sacar
[3] Extrato   
[4] Consultar saldo
"""

saques = 0
limite_saques_diarios = 3
valor_limite_por_saque = 500
saldo = 0
deposito = 0 
while True:
    print(menu)
    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        print("Obrigado por utilizar nosso sistema !")
        break
    
    # Opção para o usuário inserir um valor na sua conta    
    elif opcao == 1:
        deposito = float(input("Digite o valor que você quer depositar: "))

        if deposito <= 0:
            ("O depósito deve ser de no mínimo R$ 1.00")

        else:
            ("Depósito realizado!")
            saldo += deposito

        print(f"Seu saldo atual é de R$ {saldo:.2f}")

    # Opção para o usuário sacar um valor da sua conta
    elif opcao == 2:
       
        valor_do_saque = float(input("Qual valor você quer sacar: "))

        if (valor_do_saque > valor_limite_por_saque): 
            print(f"Você só pode sacar R$ {valor_limite_por_saque} por vez")

        elif (saques > limite_saques_diarios):
            print(f"Você ultrapassou o limite de saques diários, você tem direito a {limite_saques_diarios} por dia")

        elif (valor_do_saque > saldo):
            print(f"""
                  Saldo insuficiente!!!
                  Você tem atualmente R$ {saldo} em sua conta! 
                  """)
        else:
            print("Saque realizado")
            
            saques += 1
            saldo -= valor_do_saque

    elif opcao == 3:
        print("Extrato: ")
        print(f"""

            Você realizou {saques} saques hoje;
            Seu saldo final é de R$ {saldo:.2f}


            """)
    
    elif opcao == 4:
        print(f"Seu saldo atual é de {saldo:.2f}")

    else:
        ("Escolha uma opção válida.")