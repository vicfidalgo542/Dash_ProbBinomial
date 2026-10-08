#3)	Três em cada quatro alunos (0.75) de uma faculdade fizeram cursinho antes de prestar vestibular. Se 16 alunos são selecionados ao acaso, qual é a probabilidade de que:
import math

n = 16
p = 0.75
q = 0.25


# a) Pelo menos 12 tenham feito cursinho
def Min12():
    ProbTotal = 0

    for i in range(5):
        k = i + 12
        ProbParcial = math.comb(n, k) * (p**k) * ((1-p)**(n-k))
        print(f"Probabilidade de exatamente {k} pessoas terem feito cursinho: {ProbParcial * 100:.2f}%")
        ProbTotal += ProbParcial

    print(f"Probabilidade total de que pelo menos 12 tenham feito cursinho é de {ProbTotal * 100:.2f}%\n")
    return ProbTotal

# b) No máximo 3 não tenham feito cursinho?
def Max3Neg(p = 0.25, q = 0.75 ):
    ProbTotal = 0

    for i in range (4):
        k = i
        ProbParcial = math.comb(n, k) * (p**k) * ((1-p)**(n-k))
        print(f"Probabilidade de exatamente {k} pessoas não feito cursinho: {ProbParcial * 100:.2f}%")
        ProbTotal += ProbParcial

    print(f"Probabilidade total de que no máximo 3 tenham feito cursinho é de {ProbTotal * 100:.2f}%\n")
    return ProbTotal    



# c)	Exatamente 12 tenham feito cursinho? 
def Exat12():
    k = 12
    ProbTotal = math.comb(n, k) * (p**k) * ((1-p)**(n-k))
    print(f"Probabilidade de exatamente {k} pessoas terem feito cursinho: {ProbTotal * 100:.2f}%")
    return ProbTotal

def Respostas():
    print("Qual Questão gostaria de Ver?")
    print("1 - a) Pelo menos 12 tenham feito cursinho?")
    print("2 - b) No máximo 3 não tenham feito cursinho?")
    print("3 - c)	Exatamente 12 tenham feito cursinho? ")
    input 

    opcao = input("Digite o número da opção: ")
    
    if opcao == "1":
        Min12()
    elif opcao == "2":
        Max3Neg()
    elif opcao == "3":
        Exat12()
    else:
        print("\nInválido!\n")
        Respostas()

Respostas()