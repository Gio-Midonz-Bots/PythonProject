###Exercicio: simulação de Caixa eletrônico

saldo = 1000.00
while True:
    print("\n=== Caixa Eletrônico ===")
    print("1 - Verificar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção entre 1 à 4: "))

    if opcao == 1:
        print(f"Seu saldo é R${saldo}")
    elif opcao == 2:
        depositar = int(input("Qual é o valor que você desejar Depositar R$"))
        saldo += depositar
        print(f"Seu valor a ser depositado é: R${depositar}")
        print(f"Seu novo saldo é R${saldo}")
    elif opcao == 3:
        print(f"Seu saldo é R${saldo}")
        sacar = int(input("Qual é o valor que você desejar Sacar R$"))
        if sacar < 0:
            print("Valor negativo, tente novamente.")
        elif sacar > saldo:
            print("Valor maior que saldo, tente novamente.")
        else:
            saldo -= sacar
            print(f"Saque Realizado com sucesse \nSeu novo saldo é R${saldo}")
    elif opcao == 4:
        print("Obrigado por usar o programa!")
        break
    else:
        print("Opção invalida!, Tente novamente.")