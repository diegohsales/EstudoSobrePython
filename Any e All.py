'''
Python tem duas funções muito interessantes: ANY e ALL. 

-> A função 'ANY' recebe uma lista (ou outro objeto interável) e retorna 
'True' se algum dos elementos for avaliado como 'True'. 

-> Já 'ALL' só retorna 'True' se todos os elementos forem avaliados como 'True' ou se ainda se o iterável está vazio. Veja:

>>> everybody=[1,2,3,4]
>>> anybody=[0,1,0,2]
>>> nobody=[0,0,0,0]
>>> any(everybody)
True
>>> any(nobody)
False
>>> any(anybody)
True
>>> all(everybody)
True
>>> all(nobody) - Aqui retorno false porque o 0 significa como FALSO e o numero 1 como VERDADEIRO, pois isso no ALL dá como FALSE.
False
>>> all(anybody)
False

Sem segredos, certo? Mas essas duas funções junto com os generators permite uma sintaxe muito interessante:

>>> v=[10,12,25,14]
>>> any(n>20 for n in v)
True
>>> all(n>20 for n in v)
False

Veja um exemplo disso num código real:

if all(v<100 for v in values):
    msg='Para usar seu cupom de desconto, pelo menos '+
        'um dos produtos deve custar mais de R$ 100,00.'

E numa classe real:

class Form:
    # ...
    def validates(self):
        return not any(field.error for field in self.fields)
'''
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel'] #Deu False porque tem o nome Daniel
print(all([nome[0] == 'C' for nome in nomes]))

nomes1 = ['Carlos', 'camila', 'Carla', 'Cassiano', 'Cristina'] #Deu Treu porque todos os nomes começam com C Maiusculo
print(all([nome[0] == 'C' for nome in nomes1]))

print(all([letra for letra in 'b' if letra in 'aeiou'])) #Dá TRUE pois dá como vazio, e dá vazio pois não consta nenhuma letra. 
#Um iterável vazio convertido em boolean é FALSE, mas o all() entende como TRUE.

print(any([0,0,0,0,0,1])) #Deu TRUE pois contém o numero 1
print(any([0,0,0,0,0])) #Deu FALSE pois só contém o numero 0