MENU = """ 
####### Banco Pineapple S/A #############

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] CRIA UMA CONTA
[5] SAIR

=> """

def criar_conta():
    numero_conta = input("Digite o número da conta: ")
    titular = input("Digite o nome do titular: ")
    saldo = float(input("Digite o saldo inicial (opcional): ") or 0)
    limite = float(input("Digite o limite da conta (opcional): ") or 1000)

    nova_conta = criar_conta()
    print("Conta criada com sucesso!")
    return nova_conta


contaBancaria = []
saldo = 0
limite = 500
extrato = "" 
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(MENU)

    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$: {valor:.2f}\n"
            print("Deposito realizado com sucesso....\n")
    
        else:
         print("Valor invalido, Tente novamentE!")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Seu saldo esta baixo, não é ppssivel efetuar saques")
        
        elif excedeu_limite:
            print("Limite excedido de Saque por trasação!")

        elif excedeu_saque:
            print("Numero de saques esta litado a 3 saques por mês")       

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor: .2f}\n"  
            print("Saque realizado com sucesso!\n")
            numero_saques += 1
            print(f"Saques ja realizado no mês: {numero_saques}/3")            

        else:
            print("Operação invalida")    

    if opcao == "3":
            print("\n================= Extrato Detalhado =============\n")
            print("Não foram realizados operações." if not extrato else extrato)
            print(f"\n Saldo: R${saldo:.2f}\n")    
            print("====================================================\n")


   
   
    if opcao == "4":
        contaBancaria = criar_conta()
        break
   
    if opcao == "5":
       break
    
    
else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")
 