"""
Princípios básicos da POO ­

A Programação Orientada a Objetos se baseia em 4 pilares:
Abstração
Processo de representar entidades do mundo real
Encapsulamento
Adiciona segurança à aplicação
Herança
Facilita o reuso do código
Polimorfismo
Adicionam a possibilidade de alteração no funcionamento interno de objetos

Polimorfismo é a capacidade que um objeto possui de se comportar de diferentes formas.
Na programação orientada o objeto, o polimorfismo permite que objetos se comportem de acordo com a classe 
a que pertencem.


Herança e Polimorfismo

Herança e Polimorfismo são conceito semelhantes
Se a subclasse herda os métodos de uma superclasse e os utiliza sem nenhuma modificação, isto é conhecido como 
Herança. Se a subclasse herda os métodos de uma superclasse e os sobrescreve, ou seja, o mesmo método se 
comporta de formas diferentes em classes diferentes, isto é conhecido como Polimorfismo.
"""

class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    def consultar_saldo(self):
        print("Saldo: ", self.saldo)

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")


class ContaCorrente(Conta):
    def __init__(self, numero, titular):
        super().__init__(numero, titular)
        self.limite = 500

    def sacar(self, valor):                     # sobrescrita de método
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Erro na operação de saque")


contacorrente = ContaCorrente(1234, "Paulo")
contacorrente.depositar(100)           # executa metodo da classe mãe
contacorrente.sacar(500)               # executa metodo da classe ContaCorrente
contacorrente.consultar_saldo()        # executa metodo da classe mãe