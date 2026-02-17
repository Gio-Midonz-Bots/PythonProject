
while True:
    print("------Calculadora------")
    print("1 - adição")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - sair")
    opcao = int(input("Digite sua opção ( 1 à 5 ) "))

    if opcao == 1:
        primeiroNumero = int(input("Digite o primeiro número:"))
        segundoNumero = int(input("Digite o segundo número:"))
        resultado = primeiroNumero + segundoNumero
        print(f'O resultado da soma é {resultado}')

    elif opcao == 2:
        primeiroNumero = int(input("Digite o primeiro número:"))
        segundoNumero = int(input("Digite o segundo número:"))
        resultado = primeiroNumero - segundoNumero
        print(f'O resultado da subtração é {resultado}')
    elif opcao == 3:
        primeiroNumero = int(input("Digite o primeiro número:"))
        segundoNumero = int(input("Digite o segundo número:"))
        resultado = primeiroNumero * segundoNumero
        print(f'O resultado da multiplicação é {resultado}')
    elif opcao == 4:
        primeiroNumero = int(input("Digite o primeiro número:"))
        segundoNumero = int(input("Digite o segundo número:"))
        resultado = primeiroNumero / primeiroNumero
        print(f'O resultado da divisão é {resultado}')
    elif opcao == 5:
        print("Saindo...")
        break
    else:
        print("Tente novamente. valor errado.")
