# 4) 4)	Um sistema de segurança consiste em 4 alarmes (idênticos) de pressão alta, com probabilidade de sucesso p = 0,8 (cada um). Qual a probabilidade de se ter:
import math
n = 4 
p = 0.8
q = 0.2

# a)	Exatamente 3 alarmes soando quando a pressão atingir o valor limite? 

def Exat3():
    k = 3
    ProbTotal = math.comb(n, k) * (p**k) * ((1-p)**(n-k))

    print(f"A probabilidade de Exatamente 3 alarmes soando quando a pressão atingir o valor limite é de {ProbTotal * 100:.2f}%\n")
    return ProbTotal


#b)	Menos que 2 alarmes soando quando a pressão atingir o valor limite? 

def Low2():
    ProbTotal = 0

    for i in range(2):
        k = i
        ProbParcial = math.comb(n, k) * (p**k) * ((1-p)**(n-k))
        print(f"A probabilidade de {k} alarme/s soar/soarem quando a pressão atingir o valor limite é de {ProbParcial * 100:.2f}%\n")
        ProbTotal += ProbParcial

    print(f"A probabilidade de Menos de 2 alarmes soando quando a pressão atingir o valor limite é de {ProbTotal * 100:.2f}%\n")
    return ProbTotal




def Respostas():
    print("Qual Questão gostaria de Ver?")
    print("1 - a)	Exatamente 3 alarmes soando quando a pressão atingir o valor limite? ")
    print("2 - b)	Menos que 2 alarmes soando quando a pressão atingir o valor limite? ")

    opcao = input("Digite o número da opção: ")
    
    if opcao == "1":
        Exat3()
    elif opcao == "2":
        Low2()
    else:
        print("\nInválido!\n")
        Respostas()

Respostas()