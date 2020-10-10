"""
Crie a classe Animal com os atributos nome, cor e numero_patas. Crie também o método 
exibir_dados, que imprime na tela uma espécie de relatório informando os dados do animal.
Crie uma classe Cachorro que herda da classe Animal e que possui como atributo adicional a raça do cachorro. 
Crie também o método exibir_dados, que imprime na tela os dados do cachorro (nome, cor, numero de patas e raça)
"""

class Animal:
    def __init__(self, nome, cor, numero_patas):
        self.nome = nome
        self.cor = cor
        self.numero_patas = numero_patas

    def exibir_dados(self):
        print("--------------------")
        print("Nome:", self.nome)
        print("Cor:", self.cor)
        print("Numero de Patas:", self.numero_patas)


class Cachorro(Animal):
    def __init__(self, nome, cor, numero_patas, raca_cachorro):
        super().__init__(nome, cor, numero_patas)
        self.raca_cachorro = raca_cachorro

    def exibir_dados(self):
        super().exibir_dados()
        print("Raça Cachorro: ", self.raca_cachorro)


animal = Animal("Passarinho", "Azul", 2)
animal.exibir_dados()       # exibe os atributos do animal

dog = Cachorro("Rex", "Marrom", 4, "Vira lata")
dog.exibir_dados()          # exibe os atributos do cachorro
