for par in range(0, 16, 2):
    print(par)
print("----------------------")
for impar in range(1, 16, 2):
    print(impar)
valor = 1
for i in range(1, 6):
    multiplicacao = i * valor
    valor = multiplicacao
    print(f"multiplicando por {i}, o resultado é {multiplicacao}")
