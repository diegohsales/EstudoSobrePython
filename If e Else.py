Condições Python e instruções If

Python suporta as condições lógicas usuais da matemática:

    Igual a: a == b
    Diferente de: a! = B
    Menor que: a <b
    Menor ou igual a: a <= b
    Maior que: a> b
    Maior ou igual a: a> = b

Essas condições podem ser usadas de várias maneiras, mais comumente em "instruções if" e loops.

Uma "declaração if" é escrita usando a palavra-chave if .
Exemplo:

Declaração If:

a = 33
b = 200
if b > a:
  print("b is greater than a")

Neste exemplo, usamos duas variáveis, a e b , que são usadas como parte da instrução if para testar se b é maior que a . Como um é 33 , 
e b é 200 , sabemos que 200 é maior do que 33, e assim nós imprimir a tela que "b é maior do que a".
Recuo

Python depende de indentação (espaço em branco no início de uma linha) para definir o escopo no código. Outras linguagens de programação 
costumam usar chaves para esse propósito.
Exemplo:

Instrução If, sem recuo (gerará um erro):

a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error 