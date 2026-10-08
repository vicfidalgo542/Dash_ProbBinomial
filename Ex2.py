# 2)	Acredita-se que 20% dos moradores das proximidades de refinarias de petróleo têm alergia aos poluentes lançados ao ar. Admitindo que este percentual de alérgicos é real, calcule a probabilidade de que no máximo 3 moradores tenham alergia entre 13 selecionados ao acaso. 

import math

n = 13
p = 0.2
q = 0.8
PT = 0

for i in range(4):
    k = i 
    ProbabilidadeParcial = math.comb(n, k) * (p**k) * ((1-p)**(n-k))
    print(f"Probabilidade de {k} moradores terem alergia: {ProbabilidadeParcial * 100:.2f}%")
    PT += ProbabilidadeParcial

print(f"Probabilidade Total: {PT * 100:.2f}%\n")
