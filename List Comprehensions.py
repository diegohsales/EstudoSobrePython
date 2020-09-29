"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}

#Exemplos

numeros = {num  for num in range(1, 7)}
print(numeros)

#Outro exemplo

numeros = {x ** 2 for x in range(10)}
print(numeros)


#DESAFIO! O que pode ser feito para alterar na estrutura abaixo para gerar um dicionário ao invés de Set?
numeros = {x ** 2 for x in range(10)} #É só acrescentar um x e : na frente do outro x que ao imprimir vira um
dicionário:

print(numeros)

letras = {letra for letra in 'Geek University'} #Sem ordenação e sme repetição
print(letras)
"""









