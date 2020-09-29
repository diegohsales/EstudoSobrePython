# LISTAS:
# Sequencias de elementos. 
# Delimitada por colchetes [ ]
lista = [2, 5, 6, 10, 40]

# Listas heterogêneas: Pode conter diferentes tipos de dados 
lista = [2, 4, 5.99, 'texto', 'a']

# listas vazias
lista = []

# função print pode ser utilizada para exibir os itens contidos na lista
lista = [2, 5, 6, 90]
print(lista)

# Índice: especifica a posição de um item na lista
# Índice inicial é 0
print(lista[0])
print(lista[2])

# Índices negativos indicam posições referente ao final da lista
print(lista[-1])
print(lista[-2])

# Listas são mutáveis: podem ser alteradas
lista[0] = 'abc'
print(lista)

# append: adiciona item ao final da lista
lista.append(500)
lista.append(300)
print(lista)

# repetição for para percorrer a lista
for a in lista:
    print(a)

# preencher lista com dados informados pelo usuário
'''
lista = []
for a in range(5):
    n = int(input("Numero:"))
    lista.append(n)
print(lista)
'''
# ---------------------------------------------------
# PRINCIPAIS FUNÇÕES
print('-'*30)

# len: Retorna o tamanho de uma lista
lista = [2, 10, 7, 10]
print(len(lista))
tamanho = len(lista)
print(tamanho)

# count: Contar quantas vezes um item aparece na lista
print( lista.count(10) )

# index: Retorna o índice da primeira ocorrência de um item
# Se o item não for encontrado retorna uma exceção
lista = [2, 10, 5, 10, 99]
print( lista.index(10) )
# print( lista.index(50) )

# in: verificar se determinado item existe em uma lista
if 10 in lista:
    print("O numero 10 está na lista")

if 500 not in lista:
    print("O numero 500 não está na lista")

if 500 in lista:
    print( lista.index(500))
else:
    print("O numero 500 nao existe na lista")

# insert: insere item em determinada posição
lista = [1, 2, 3]
lista.insert(1, 50)
print(lista)

# pop: Remove o último item da lista
lista.pop()
print(lista)

# pop: Remove um item pelo indice
lista.pop(0)
print(lista)

# remove: Remove primeira ocorrencia da lista
lista = [1, 3, 60, 10, 60, 60, 60]
lista.remove(60)
print(lista)

while 60 in lista:
    lista.remove(60)
print(lista)

# sort: ordenação da lista
lista = [100, 50, 1, -5, 300]
lista.sort()
print(lista)

lista.sort(reverse=True)
print(lista)

# reverse: inverte a lista
lista = [3, 5, 300, 100]
lista.reverse()
print(lista)

# min: menor elemento
print(min(lista))

# max: maior elemento
print(max(lista))

# sum: somatorio da lista
print(sum(lista))

# exemplo de calculo de média
media = sum(lista) / len(lista)
print(media)

# concatenação de listas
a = [3, 50, 7]
b = [7, 20, 7]
c = a + b
print(c)
d = c + a
print(d)

# cópia de lista
a = [1, 2, 3]
b = a               
print(a)
print(b)
a.append(100)
print(a)
print(b)

d = []
d = d + a
d.append(500)
print(a)
print(d)


# listas bidimensionais
lista = [ [1,2,3], [4,5,6] ]
print(lista)
lista[1][2] = 200
print(lista)

# ----------------------------------------------
# TUPLAS

# Sequencias de elementos que não podem ser alteradas
# Delimitada por parenteses ( )
tupla = (1, 5, 7)

# tuplas vazias
tupla = ()
print(tupla)

# tuplas de 1 elemento (tem uma virgula no final)
tupla = (1,)
print(tupla)

# acesso pelo índice
tupla = (4, 6, 60)
print(tupla[1])

# percorre tupla
for a in tupla:
    print(a)

# concatenção de tuplas
a = (3, 5, 2)
b = (2, 60, 7)
c = a + b
print(c)

# preenchimento de tuplas pelo usuário
tupla = ()
for a in range(5):
    n = int(input("Numero: "))
    tupla = tupla + (n,)
print(tupla)