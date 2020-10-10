"""
Implemente a classe Filme, conforme o diagrama de classes abaixo
Todos os atributos devem ser privados
Crie os métodos get e set para todos os atributos

No seu programa principal, faça a seguinte implementação:
Criar uma lista de filmes vazia
Cadastrar 3 filmes (com os dados informados pelo usuário)
Armazenar os dados de cada filme em um objeto da classe Filme
Armazenar os objetos na lista de filmes
Exibir um relatório com os dados de todos os filmes cadastrados
"""


class Filme:
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_genero(self, genero):
        self.__genero = genero


lista = []
for i in range(3):
    titulo = input("Titulo: ")
    genero = input("Genero: ")
    filme = Filme(titulo, genero)
    lista.append(filme)

print("Lista de filmes: ")
for filme in lista:
    print("Titulo: ", filme.get_titulo())
    print("Genero: ", filme.get_genero())