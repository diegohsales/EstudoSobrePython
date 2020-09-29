"""
Utilizando Lambdas!

Comhecidas por expressões lambdas ou simplesmente lambdas, são funções sem nome, ou seja, funções anonimas.

#Função em Python

def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

#Função Lambda
lambda x: 3 * x + 1

# E como utilizar a expressão lambda?
#Como ela é uma expressão "sem nome", para utilizar ela podemos dar qualquer nome.

calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

DICA: Função STRIP reduz o espaço no inicio e no fim, ou seja, ele tira espaço do inicio e do fim de uma string.
ex:
' Diego ' sem strip
'Diego' com strip

#Podemos ter expressões lambdas com múltiplas entradas.

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' diego ', ' henrique'))

Em funções Python podemos ter nenhuma entrada ou várias entradas. Em lambdas também.

amar = lambda: 'Como não amar Python?'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0,5

tres = lambda x, y, z: 3 / (1 / x + 1 / y +1 / z)

#n = lambda x1, x1, ...., xn: <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

#OBS Se passarmos mais argumentos do que parâmetros esperados teremos TypeError
"""

