## Problema das sarnas

# Neste problema temos de encontrar a árvore de suporte de custo mínimo que liga as sardas.
# Para saber a distâcia da sarda(x1,y1) a (x2,y2) , basta usar √(x1-x2)² + (y1-y2)²
# Tanto pode usar o algoritmo de Prim, como o algoritmo de Kruskal. Uma sugestão é implementar ambos e verificar que dão a mesma resposta.

# Vamos representar cada sarda (vértice) por um dicionário com suas respectivas coordenadas:

sarda_1 = {'coord_x1': 1.000, 'coord_y1': 1.000}
sarda_2 = {'coord_x2': 2.000, 'coord_y2': 2.000}
sarda_3 = {'coord_x3': 2.000, 'coord_y3': 4.000}


# Distância entre sarda 1 e sarda 2

from math import *
    
dist_sd_1_2 = (sarda_1['coord_x1'] - sarda_2['coord_x2']) ** 2 + (sarda_1['coord_y1'] - sarda_2['coord_y2']) ** 2
distancia_1_2 = sqrt(dist_sd_1_2) # calcula raiz quadrada
print(f'A distância entre os 2 pontos {distancia_1_2:.3f}')


# Distância entre sarda 1 e sarda 3:

dist_sd_1_3 = (sarda_1['coord_x1'] - sarda_3['coord_x3']) ** 2 + (sarda_1['coord_y1'] - sarda_3['coord_y3']) ** 2
distancia_1_3 = sqrt(dist_sd_1_3)
print(f'A distância entre os 2 pontos {distancia_1_3:.3f}')


# Distância entre sarda 2 e sarda 3:

dist_sd_2_3 = (sarda_2['coord_x2'] - sarda_3['coord_x3']) ** 2 + (sarda_3['coord_y3'] - sarda_2['coord_y2']) ** 2
distancia_2_3 = sqrt(dist_sd_2_3)
print(f'A distância entre os 2 pontos {distancia_2_3:.3f}')


# Algoritmo de Kruskal para achar a árvore geradora mínima

floresta = [sarda_1, sarda_2, sarda_3] # Meus vértices (sardas)
conjunto = [distancia_1_2, distancia_1_3, distancia_2_3]

# Enquanto conjunto for não-vazio, remove-se uma aresta com peso mínimo desse conjuntos

while len(conjunto) != 0:
    conjunto.remove(max(conjunto)) # Essa aresta tem peso mínimo
    break

    
soma = 0

for item in conjunto:
    soma += item
    
print(f'A quantidade de tinta que Sara deve gastar: {soma:.3f}')
