""""
def cantar_parabens(aniversariante):
    print('Parabens pra você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o {aniversariante}!')

cantar_parabens('Diego') # não vai dar erro porque foi informado um parametro

cantar_parabens() #vai dar erro porque não foi informado nenhum parametro TypeError

#Funções podem ter N parametros de entrada.
#Exemplos

def soma(a, b):
    return a + b

def multiplica(num1 , num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg #ele soma o num1 e B e multiplcia a msg de parametro de entrada

print(soma(2, 5))
print(soma(10, 20))
print(soma(10, 20, 30)) #vai dar erro pois na definição da função foi informado somente 2 parametros e não 3.
#TypeError: soma() takes 2 positional arguments but 3 were given
print(soma(10)) #vai dar erro também porque passamos argumentos a menos do que informado na entrada.


print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'Geek '))
print(outra(4, 5, 'Python '))
print(outra('Geek', 2, 2)) #vai dar erro de TyError

#Nomeando parametros

def nome_completo(nome, sobrenome): #parametro
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Diego', "Henrique")) #argumentos

#A diferença entra parametro e argumento

#Parametro: são variaveis declaradas na definição de uma função.
#Argumento: são dados passados durante a execução de uma função.


#A ordem dos parametro importa!

nome = 'Diego'
sobrenome = 'Henrique'

print(nome_completo(sobrenome, nome))

def soma_impares(numeros):
    total = 0
    for num in numeros: #para cada num em numeros
        if num % 2 != 0: #se o num for modulo por 2 for diferente de 0
            total = total + num #vai somar o total que é 0 mais o numeros
    return total

lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista))
"""
def soma_pares(numeros):
    total = 0
    for num in numeros: #para cada num em numeros
        if num % 2 != 1: #se o num for modulo por 2 for diferente de 0
            total = total + num #vai somar o total que é 0 mais o numeros
    return total

lista = [1, 2, 3, 4, 5, 6, 7]

print(soma_pares(lista))






