"""
Classe Abstrata x Classe Concreta:

Classe concreta é uma classe que pode ser instanciada diretamente (as que vimos até agora)

Classe abstrata é uma classe que não pode ser instanciada diretamente.
São classes feitas especialmente para serem modelos para suas classes filhas.

Qual a vantagem de uma classe abstrata? 
Por enquanto, a única diferença é que não podemos instanciar um objeto da classe abstrata.
Uma classe abstrata pode servir para agrupar informações comuns às classes filhas, quando não faz sentido existir na aplicação objetos instanciados diretamente dela

A decisão de transformar uma classe em abstrata depende do domínio do problema. 
Pode ser que, em um sistema com classes similares, faça sentido que uma classe similar seja concreta.

Métodos Abstratos
Na prática, classes abstratas definem um modelo para as suas classes filhas
Para isso, uma classe abstrata pode ter métodos abstratos

Método abstrato é um método que não possui implementação.
As classes filhas são obrigadas a implementar os métodos abstratos da classe mãe
"""

from abc import ABC, abstractmethod         # importar modulo


class Conta(ABC):                  # classe abstrata (não pode ser instanciada)
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    @abstractmethod                # metodo abstrato (não possui implementação)
    def sacar(self, valor):
        pass

    @abstractmethod                # metodo abstrato (não possui implementação)
    def depositar(self, valor):
        pass

    def consultar_saldo(self):     # metodo concreto
        print("Saldo:", self.saldo)


# É obrigatorio sobrescrever os metodos abstratos em todas as classes filhas
class Poupanca(Conta):
    def __init__(self, numero, titular):
        super().__init__(numero, titular)

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Erro: Saldo Insuficiente")

    def depositar(self, valor):
        self.saldo += valor


class ContaCorrente(Conta):
    def __init__(self, numero, titular):
        super().__init__(numero, titular)
        self.limite = 500

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Erro: Saldo Insuficiente")

    def depositar(self, valor):
        self.saldo += valor


c = Poupanca(123, "Paulo")
c.depositar(100)
c.sacar(50)
c.consultar_saldo()