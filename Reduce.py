'''
A função reduce, disponível no módulo built-in functools, serve pra "reduzir" um iterável (como uma lista) a um único valor.
É um paradigma um pouco mais comum em linguagens funcionais, mas que também é bastante útil em linguagens imperativas/orientadas a 
objetos como o Python.

Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o itirável.

'reduce(funcao, dados)'

Mas como assim, "reduz" uma lista?
Suponhamos que você tem uma lista minha_lista, que só contém números, e que você queira o resultado da multiplicação entre todos 
esses números. Um dos jeitos de fazer isso é com um for:
'''
# Queremos 2 * 4 * 5 * 2, que é igual a 80
minha_lista = [2, 4, 5, 2]

produto_total = 1
for numero in minha_lista:
     produto_total *= numero

print(produto_total)  # 80
'''
Isso funciona, mas também pode ser feito com reduce:
'''
from functools import reduce #importando o reduce.

minha_lista = [2, 4, 5, 2]

def mult(x, y):
    return x * y

produto_total = reduce(mult, minha_lista)
print(produto_total)  # 80

'''
Ou, de modo equivalente mas um pouco mais conciso, com uma função lambda (que nada mais é do que uma função definida em uma só 
expressão/linha):
'''
from functools import reduce

minha_lista = [2, 4, 5, 2]

produto_total = reduce(lambda x, y: x * y, minha_lista)
print(produto_total)  # 80

'''
Então o que está acontecendo aí? Se dermos uma olhada em "slow motion", o que acontece é o seguinte:

    reduce recebe como argumento de função aplicada a função mult (ou a lambda, no segundo caso)
    reduce recebe como iterável a lista minha_lista
    reduce considera como x e y, respectivamente, os dois primeiros elementos de minha_lista: 2 e 4
    reduce aplica a x e y a função mult, que multiplica um pelo outro: em 2 * 4, o resultado é 8.
    O resultado da aplicação da função (nosso 8) passa a ser x, e o próximo elemento não processado (5, terceiro elemento da nossa 
    lista) passa a ser y
    A função mult é aplicada a x e y: 8 * 5 retorna 40, e esse valor retornado passa a ser nosso novo x

    A função mult é aplicada pela última vez ao x e o último elemento da nossa lista, 2. 40 * 2 nos retorna 80
    Como não há mais elementos em que aplicar a função, reduce nos retorna o resultado final: 80, como esperado.

Resumindo, a função aplica outra função sequencialmente e cumulativamente a uma lista (iterador), e "reduz" a lista a um só 
resultado final.

Outro exemplo didático é o de calcular o valor mínimo de uma lista:
'''
from functools import reduce

minha_lista = [2, 4, 5, 2, 1]

def achar_minimo(x, y):
    if x < y:
        return x
    else:
        return y

minimo = reduce(achar_minimo, minha_lista)
print(minimo)  # 1

'''
Nesse caso, o primeiro argumento x é usado pra guardar o menor valor visto, e ele é comparado com os outros valores y da lista.

Digo que esse exemplo é didático porque já existe uma função equivalente no Python: a min. Ainda assim, acho que o exemplo é legal 
pra dar outra ideia do poder de reduce.

Além do mostrado acima, o reduce também aceita um terceiro argumento opcional, o initial_value. Como o nome indica, esse argumento 
pode ser dado como valor inicial, e é em efeito a mesma coisa do que botar esse valor no início da sua lista.

Esses exemplos são simples e podem parecer bobos, mas à medida que as funções aplicadas ficam mais complexas, usar o reduce pode 
ser uma boa pra diminuir o tamanho do código e deixá-lo mais claro. De qualquer modo, é uma boa ferramenta a se ter.
'''