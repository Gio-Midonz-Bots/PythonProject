import random

numeroSecreto1 = random.randint(1, 10)
numeroSecreto2 = random.randint(1, 10)

tentativas = 5
adivinhou1 = False
advinhou2 = False
while tentativas > 0 and (not adivinhou1 or not advinhou2):
    print(f"Tentativas: {tentativas}")
    tentativas -= 1
    palpite1 = int(input("Adivinhe o Primeiro numero entre 1 e 10: "))
    palpite2 = int(input("Adivinhe o Segundo  numero entre 1 e 10: "))
    if palpite1 == numeroSecreto1:
        print("VocÊ Acertou o primeiro numero!")
        adivinhou1 = True
    if palpite2 == numeroSecreto2:
        print("VocÊ acertou o segundo numero!")
        advinhou2 = True
    else:
        print("Tente novamente.")

print(f"O numero secreto: {numeroSecreto1}, {numeroSecreto2}")