# 5)	Um engenheiro de inspeção extrai uma amostra de 15 itens aleatoriamente de um processo de fabricação sabido produzir 85% de itens aceitáveis. 

import math

n = 15
p = 0.85
q = 0.15

def Exat10():
    k = 10
    ProbTotal = math.comb(n, k) * (p**k) * ((1-p)**(n-k))

    print(f"A probabilidade de que 10 dos itens extraídos sejam aceitáveis é de {ProbTotal * 100:.2f}%\n")
    return ProbTotal


def Low3Neg():
    ProbTotal = 0
    p = 0.15

    for i in range(3):
        k = i
        ProbParcial = math.comb(n, k) * (p**k) * ((1-p)**(n-k))
        print(f"A probabilidade de {k} item/ns não ser/serem aceitável/eis é de {ProbParcial * 100:.2f}%\n")
        ProbTotal += ProbParcial

    print(f"A probabilidade de que menos que três não sejam aceitáveis é de {ProbTotal * 100:.2f}%\n")
    return ProbTotal


def Respostas():
    print("Qual Questão gostaria de Ver?")
    print("1 - a) Qual a probabilidade de que 10 dos itens extraídos sejam aceitáveis?")
    print("2 - b) Qual a probabilidade de que menos que três não sejam aceitáveis?")

    opcao = input("Digite o número da opção: ")
    
    if opcao == "1":
        Exat10()
    elif opcao == "2":
        Low3Neg()
    else:
        print("\nInválido!\n")
        Respostas()

Respostas()
