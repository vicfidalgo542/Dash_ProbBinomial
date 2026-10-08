# 1)	Uma empresa de confecção de uniformes suspeita que 30% de sua produção apresenta algum defeito. Se tal suspeita é correta, determine a probabilidade de que, numa amostra de quatro peças, sejam encontradas:
import math

n = 4
p = 0.3
q = 0.7
k = ''

# a)	No mínimo duas peças com defeitos; 
import math

def probabilidade_minimo_duas(n, p):
    prob_A = 0
    
    for i in range(3):
        k = i + 2
        probabilidadeParcial = math.comb(n, k) * (p**k) * ((1-p)**(n-k))
        print(f"Probabilidade de {k} peças ruins: {probabilidadeParcial * 100:.2f}%")
        prob_A += probabilidadeParcial
        
    print(f"Probabilidade Total: {prob_A * 100:.2f}%\n")
    return prob_A

# b)	Menos que duas peças boas;

def probabilidade_menos_duas_boas(n, p):
    prob_B = 0
    p = 0.7 #invertemos a pergunta
    q = 0.3

    for i in range(2):
        k = i
        probabilidadeParcial = math.comb(n, k) * (p**k) * ((1-p)**(n-k))
        print(f"Probabilidade de {k} peças boas: {probabilidadeParcial * 100:.2f}%")
        prob_B += probabilidadeParcial

    print(f"Probabilidade Total: {prob_B * 100:.2f}%\n")
    return prob_B

# c) Nenhuma peça com Defeito

def Sem_defeitos (n, p):
    k = 0
    p = 0.3
    q = 0.7

    prob_C = math.comb(n, k) * (p**k) * ((1-p)**(n-k))
    print(f"Probabilidade de {k} peças com defeito: {prob_C * 100:.2f}%\n")
    return prob_C


#probabilidade_minimo_duas(4, 0.3)
#probabilidade_menos_duas_boas(4, 0.7)
#Sem_defeitos(4, 0.3)
