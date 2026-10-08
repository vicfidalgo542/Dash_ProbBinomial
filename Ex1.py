# 1)	Uma empresa de confecção de uniformes suspeita que 30% de sua produção apresenta algum defeito. Se tal suspeita é correta, determine a probabilidade de que, numa amostra de quatro peças, sejam encontradas:
import math

n = 4
p = 0.3
q = 0.7
k = ''

# a)	No mínimo duas peças com defeitos; 
import math

def calcular_probabilidade_minimo_duas(n, p):
    prob_A = 0
    
    for i in range(3):
        k = i + 2
        probabilidadeParcial = math.comb(n, k) * (p**k) * ((1-p)**(n-k))
        print(f"Probabilidade de {k} sucessos: {probabilidadeParcial * 100:.2f}%")
        prob_A += probabilidadeParcial
        
    print(f"Probabilidade Total: {prob_A * 100:.2f}%\n")
    return prob_A

# b)	Menos que duas peças boas;
