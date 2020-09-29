"""
Entendendo o *args

- O *args é um parâmetro  como outro qualquer. Isso significa que você poderá chamar
de qualquer coisa, desde que começe com asterisco.
Por meio da convenção foi definido que seria utilizado desse maneira *args.

Mas o que é *args?

O Parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada
em um tupla. Então desde já lembre-se que as tuplas são imutáveis.

# Exemplo do que não é legal

def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4

print(soma_todos_numeros(4, 6, 9))
print(soma_todos_numeros(4, 6))
print(soma_todos_numeros(4, 6, 9, 5))

# Entendendo o args

def soma_todos_numeros(*args):
    print(args)

soma_todos_numeros()
soma_todos_numeros(1)
soma_todos_numeros(2, 3)
soma_todos_numeros(2, 3, 4)
soma_todos_numeros(3, 4, 5, 6)

def soma_todos_numeros(*args):
    return sum(args)

    #total = 0
    #for numero in args:
     #   total = total + numero
    #return total

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))

print(soma_todos_numeros(23.4 + 13.5))


# Outro exmplo da utilização do args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza de quem você é...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

def soma_todos_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7] #TypeErros não é possivel fazer operação com essa lista


# Desempacotador

print(soma_todos_numeros(*numeros))

#OBS: O asteristico serve para que informemos ao Python que estamos passando
como argumento uma coleção de dados. Desde forma, ele saberá que
precisará antes desempacotar estes dados.

---------------------------------------------------------------------------------------------
Entendendo o **Kwargs

Poderiamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs.

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma
tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras
em um dicionário.

#Exemplos

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}') #função title() deixa a primeira letra Maiscula


cores_favoritas(marcos='Verde', julia='amarelo', fernanda='azul', vanessa='branco')

#OBS: Os parâmetros *args e o **kwargs não são obrigatorios.

#Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

Nas nossas funções, podemos ter: (tem que ser nessa ordem)

- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios)
- **kwargs

*Parâmetro Correto

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

#Entenda por quê é importante manter a ordem dos parâmetros na declaração:

#Função com a ordem correta de parâmetro
#def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
 #   return [a, b, args, instrutor, kwargs]

#Função com a ordem incorreta de parâmetro

def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Desempacotar com o **kwargs - desempacotamos apartir do duplo asteristico.

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Diego', 'sobrenome': 'Henrique'}

print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

OBS: Os nomes da chave em um dicionário devem ser o mesmo dos parâmetros da função

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

dicionario = dict(d=1, e=2, f=3) #TypeError pois os nomes das chaves estão diferentes dos parâmetros da função.
TypeError: : soma_multiplos_numeros() got an unexpected keyword argument 'd'

soma_multiplos_numeros(**dicionario)

"""