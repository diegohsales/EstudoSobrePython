"""
Filter

Quando trabalhamos com Python e utiliza essa linguagem Python e utiliza essa linguagem para ciência de dados
biotecnologia e inteligência artificial (IA), vai passar muito tempo trabalhando com coleções de dados.

Grandes vantagens de se utilizar Python é o poder praticamente infinito de realizar tarefas como se fosse mágica,
e facilmente conseguimos desenvolver tarefas que poderiam ser complexas em outras linguagens de programação,
e uma dessas tarefas que pode se trabalhar poderia ser a de selecionar certo grupo de dados de alguma coleção ou seja,
filtrar nossos dados, e é ai que entrar o 'FILTER'.

filter() -> Serve para filtrar dados de uma determinada coleção.

Imagine que temos uma coleção de dados no Spotify ou qualquer outro tipo de serviço que tenha lá o titulo da
musica e a quantidde de vezes que a musica foi tocada. E você deseja fazer um top 10 das músicas mais tocadas, e
vamos precisas fazer um filtro desses dados, ou seja precisamos fazer uma seleção dessas 10 musicas mais tocadas e
é isso que o 'Filter' faz.

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor:
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

#OBS - Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável.

res = filter(lambda x: x > media, dados) ->
# Lambda recebe um parâmetro de entrada que é os parâmetros dados e
#filtrar todos os numeros que são maiores que o resultado da média.
print(list(res))

#OBS -> Assim como na função map(), após serem utilizados os dados de filter() eles são excluidos da memoria.

Uma outra utilização do 'filter()' é a remoção de dados faltantes que claro é também muito utilizada em ciência
de dados e inteligência artificial (IA).

O que seria dados faltantes?

São listas ou outro tipo, que contém dados faltantes dentro dessas listas ou variaveis. Porém não é muito interessante
fazer nenhum tipo de processamento de dados seja em ciência de dados, data science ou seja em inteligência artificial
com dados faltantes, pois vai distorcer no resultado final. Por isso é de costume fazer filtros para remover esses
dados faltantes.
Ex:

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '','', 'Venezuela']
print(paises) # Imprimir tudo até os vazios.

# Fomra 1
res = filter(None, paises) # None é o tipo vázio, por isso a função filter vai filtrar tudo que for vazio de paises.
print(list(res))

# Forma 2
res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

# Forma 3
res = filter(lambda pais: pais != '', paises)
print(list(res))

E qual a diferença de filter() e map() ?
A diferença é:

Na map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada
elemento de iterável.

No filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos
de acordo com a função.

Na verdade a diferença entre os dois é o tipo de função a ser utilizada. Mas se prestarmos a atenção um pouco mais
detalhes você vai ver que a função do filter() sempre retorna ou TRUE ou FALSE valores booleonos.
Já o map() não, a função retorna valores, outros valores que não sejam TRUE e nem FALSE.

# Exemplos mais complexo:

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "tweets": ["Eu amo gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "Samuel", "tweets": ["Eu gosto de cachorros", "Eu vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

# Combinar filter() e map():

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contento 'Sua instrutura é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
"""














