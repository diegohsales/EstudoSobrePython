"""
Herança

Herança é um princípio da programação orientada a objetos (POO) que permite criar uma nova classe a partir de uma já existente.
º Chama-se “herança” porque a nova classe herda os métodos e atributos de uma classe já existente
º A principal vantagem de usar herança é a reutilização do código. 
º Esse reaproveitamento pode ser acionado quando se identifica que o atributo ou método de uma classe será igual para as outras.
"""
"""
Exemplo 01

class Veiculo:
    def __init__(self, marca, modelo, ano_fabricacao):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacao = ano_fabricacao

    def imprimir_informacoes(self):
        print("--------------------")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Ano fabricação:", self.ano_fabricacao)


# Carro herda Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, quantidade_porta):
        # super() - chama o construtor da classe mãe
        super().__init__(marca, modelo, ano_fabricacao)
        self.quantidade_porta = quantidade_porta

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print('Portas: ', self.quantidade_porta)


# Moto herda Veiculo
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, partida_eletrica):
        super().__init__(marca, modelo, ano_fabricacao)
        self.partida_eletrica = partida_eletrica

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print('Partida Eletrica: ', self.partida_eletrica)


# cria objeto Carro
carro1 = Carro("Ford", "Ka", 2015, 4)
carro1.imprimir_informacoes()

# cria um objeto Moto
moto1 = Moto("Honda", "Biz", 2013, 'sim')
moto1.imprimir_informacoes()

# cria um objeto Veiculo
veic = Veiculo("marca", "modelo", 2010)
veic.imprimir_informacoes()
---------------------------------------------------------------------------------------------
Exemplo 02
class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir_dados(self):
        print("--------------------")
        print("Nome:", self.nome)
        print("Email:", self.email)
        print("Telefone:", self.telefone)


class Aluno(Pessoa):
    def __init__(self, nome, email, telefone, ra, turma):
        super().__init__(nome, email, telefone)
        self.ra = ra
        self.turma = turma

    def exibir_dados(self):
        super().exibir_dados()
        print("RA: ", self.ra)
        print("Turma:", self.turma)


class Professor(Pessoa):
    def __init__(self, nome, email, telefone, salario):
        super().__init__(nome, email, telefone)
        self.salario = salario

    def exibir_dados(self):
        super().exibir_dados()
        print("Salario:", self.salario)


aluno1 = Aluno("Pedro", "pedro@email.com", 188888, 1234, "ADS2D")
professor1 = Professor("João", "joao@email.com", 11888888, 2000.0)
aluno1.exibir_dados()
professor1.exibir_dados()
"""
"""
Herança Multipla
Herança multipla é quando a classe mãe herda mais de uma classe, exemplo:
Anfibio herda da classe Animal Terreste e Animal Aquatico.

Exemplo 01:

class AnimalTerrestre:
    def __init__(self):
        self.habitat = 'Terra'

    def andar(self):
        print('Animal Terrestre Andando')

    def comer(self):
        print('Animal Terrestre Comendo')


class AnimalAquatico:
    def __init__(self):
        self.habitat = 'Agua'

    def nadar(self):
        print('Animal Aquatico Nadando')

    def comer(self):
        print('Animal Aquatico Comendo')


class Anfibio(AnimalAquatico, AnimalTerrestre):
    def __init__(self, nome):
        AnimalAquatico.__init__(self)
        AnimalTerrestre.__init__(self)
        self.nome = nome


animal = Anfibio()
animal.andar()
animal.nadar()
animal.comer()

Exemplo 02

class Portugues:
    def dizer_oi(self):
        print('Oi!')

    def dizer_tchau(self):
        print('Tchau!')


class Ingles:
    def dizer_oi(self):
        print('Hi!')

    def dizer_tchau(self):
        print('Bye!')

    def dizer_alguma_coisa(self):
        print('something')


class Bilingue(Portugues, Ingles):
    def dizer_oi(self):
        Portugues.dizer_oi(self)
        Ingles.dizer_oi(self)


pessoa = Bilingue()
pessoa.dizer_oi()
pessoa.dizer_tchau()
pessoa.dizer_alguma_coisa()

"""
