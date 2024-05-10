nome = (input("Digite seu primeiro nome:"))
sobrenome = (input("Digite seu seu sobrenome:"))

print(f"Bom dia Sr(a){nome.title()} {sobrenome.title()} abaixo estão as suas opçoes em nosso banco:")


mensagem = f'''
################# MENU BANCO PESSOAL ###################

                   Opção 1 Depósito
                   Opção 2 Saque
                   Opção 3 Extrato
                   Opção 0 Sair

########################################################
                   
'''
saldo = 0
option = -1
while option != 0:
    option = int(input(mensagem))

    if option ==1:
        valor = int(input("Qual o valor do depósito: "))
        saldo = valor + saldo
        print(f"Deposito de R${valor:.2f} realizado. Saldo atual: R${saldo:.2f}")
   
    elif option == 2:
        saque = int(input("Qual o valor do saque: "))
        if saldo < saque:
            print("Voce nao possui saldo suficiente")
        else:
            saldo = saldo - saque    
            print(f"Saque de R${saque:.2f} realizado. Saldo atual: R${saldo:.2f}")
    
    elif option ==3:
        print(f"O seu extrato é: ", saldo)

else:
    print("Voce saiu do sistema")

