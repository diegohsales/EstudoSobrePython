"""
Exercício Python 4: 
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e 
todas as informações possíveis sobre ele.
"""
a = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaço: ', a.isspace())
print('É um numero: ', a.isnumeric())
print('É alfabetico: ', a.isalpha())
print('É alfanumerico: ', a.isalnum())
print('Está em maiscula: ', a.isupper())
print('Está em minuscula: ', a.islower())
print('Esta capitalizada: ', a.istitle())

"""
Exercício Python 5: 
Faça um programa que leia um número Inteiro e mostre na tela 
o seu sucessor e seu antecessor.
"""
n = int(input('Digite um numero: '))
a = n - 1
s = n + 1

print('Analisando o valor {}, seu antecessor é {}, e seu sucessor é {}'.format(n, a, s))
print('Analisando o valor {}, seu antecessor é {}, e seu sucessor é {}'.format(n, (n-1), (n+1)))

"""
Exercício Python 6: 
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro de {} vale {}'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}'.format(n, (n*3), n, (n**(1/2))))