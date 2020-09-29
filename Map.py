"""
Map


Com Map, fazemos mapeamentos de valores para função.

import math

def area(r):
    # Calcula a area de um circulo com um raio 'r'. #
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

#Forma Comum de calcular a área

areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

#Forma 2 utilizando MAP
# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável. Retorna um Map Object.

areas = map(area, raios)
print(list(areas))

#Forma 3 - Map com Lambda

print(list(map(lambda r: math.pi *  (r ** 2), (raios))))

#Após utilizar a função Map depois da primeira utilização do resultado, ele zera.

# Para Fixar - Map

Temos dados iteráveis:

- Dados: a1. a2, ..., an

Temos uma função:

-Função: f(x)

 Utilizando a função map(f, dados), onde map irá mapear cada elemento dos dados e aplicar a função.

 o Map object: f(a1), f(a2), f(...), f(an)

 #Mais um exemplo

cidades = [('Berlin', 29), ('Cairo', 36), ('Bueno Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova york', 28),
           ('Londres', 22)]

print(cidades)

# f = 9/5 * c + 32
# Lambda

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))
"""