Loops Python

Python tem dois comandos de loop primitivos:

    while loops
    for loops

The while Loop

Com o enquanto ciclo podemos executar um conjunto de instruções enquanto uma condição for verdadeira.
Exemplo

Imprima i, desde que i seja menor que 6:

i = 1
while i < 6:
  print(i)
  i += 1

Nota: lembre-se de incrementar i, ou então o loop continuará para sempre.

O enquanto circuito requer variáveis relevantes para estar pronto, neste exemplo, é necessário definir uma variável de indexação, i , 
que definido como um.
A declaração de quebra

Com a instrução break , podemos parar o loop mesmo se a condição while for verdadeira:
Exemplo:

Saia do loop quando i for 3:

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 

#Python For Loops

Um por laço é utilizado para a iteração através de uma sequência (isto é, quer uma lista, um tuplo, um dicionário, de um conjunto, ou 
uma cadeia).

Isso é menos parecido com a palavra-chave for em outras linguagens de programação e funciona mais como um método iterador encontrado 
em outras linguagens de programação orientadas a objetos.

Com o loop for , podemos executar um conjunto de instruções, uma vez para cada item em uma lista, tupla, conjunto etc.


Imprima cada fruta em uma lista de frutas:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

O de ciclo não requer uma variável de indexação para definir de antemão.
Looping através de uma corda

Mesmo strings são objetos iteráveis, eles contêm uma sequência de caracteres:


Faça um loop pelas letras da palavra "banana":

for x in "banana":
  print(x)
A declaração de quebra

Com a instrução break , podemos interromper o loop antes que ele percorra todos os itens:


Saia do loop quando xfor "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break


Saia do loop quando xfor "banana", mas desta vez o intervalo vem antes da impressão:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)