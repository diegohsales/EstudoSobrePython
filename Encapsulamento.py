"""
Encapsulamento
º Encapsulamento diz respeito à proteção dos atributos ou métodos de uma classe
º Consiste em separar aspectos externos de um objeto dos detalhes internos de implementação
º Evita que dados específicos de uma aplicação possa ser acessado diretamente

Em Python, ao aplicar o conceito de encapsulamento, os atributos e métodos podem ser:
º Públicos
º Privados

Atributos ou métodos com nomes iniciados por dois sublinhados são privados e todas as outras formas são públicas.
Os atributos ou métodos privados não podem ser acessados fora da classe.

a prática mais comum é criar dois métodos:
- um que retorna o valor do atributo (get)
- e outro que altera o valor do atributo (set)

A convenção para esses métodos em muitas linguagens orientadas a objetos é colocar a palavra get ou set antes do nome do atributo.

Métodos get: retorna valor do atributo
Métodos set: Altera o valor do atributo

Representação no Diagrama de Classes:
O símbolo + representa um atributo ou método público
O símbolo - representa um atributo ou método privado

|-------------------|
|      Pessoa       |
|-------------------|
|+ nome: str        |
|+ idade: int       |
|- cpf: str         |
|- rg: str          |
|-------------------|
| + get_cpf()       |
| + get_rg()        |
| + set_cpf(cpf)    |
| + set_rg(rg)      |
|-------------------|
"""
Exemplo 01:

class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf        # Atributo Privado
        self.__rg = rg          # Atributo Privado

    # Métodos Get
    def get_cpf(self):
        return self.__cpf

    def get_rg(self):
        return self.__rg

    # Métodos Set
    def set_cpf(self, cpf):
        if len(cpf) == 11:      # Valida CPF
            self.__cpf = cpf
        else:
            print("Valor Inválido")

    def set_rg(self, rg):
        self.__rg = rg


pessoa1 = Pessoa("João", 25, "11111111111", "3333333")
pessoa1.idade = 26                      # Altera a idade
pessoa1.set_cpf("22222222222")          # Altera cpf

print("Nome: ", pessoa1.nome)
print("CPF:", pessoa1.get_cpf())        # Exibe CPF

Exemplo 02

class Funcionario:
    def __init__(self, nome, idade, salario):
        # atributos publicos
        self.nome = nome
        self.idade = idade
        # atributo privado
        self.__salario = salario

    # GET - retornar o valor de um atributo
    def get_salario(self):
        return self.__salario

    # SET - altera o valor de um atributo
    def set_salario(self, novosalario):
        if novosalario > self.__salario:
            self.__salario = novosalario
        else:
            print('Valor Invalido')


joao = Funcionario('João Silva', 25, 1500.00)
maria = Funcionario('Maria Carolina', 27, 2000.00)

print(joao.get_salario())
joao.set_salario(1000.00)
print(joao.get_salario())
joao.set_salario(3000)
print(joao.get_salario())

Exemplo 03

class ContaBancaria:
    def __init__(self, numero, titular, senha):
        self.numero = numero
        self.titular = titular
        self.__senha = senha
        self.__saldo = 0

    def get_saldo(self, senha):
        if senha == self.__senha:
            return self.__saldo
        else:
            print('Senha invalida')

    def depositar(self, valor, senha):
        if senha == self.__senha:
            self.__saldo += valor
        else:
            print('Senha invalida')

    def sacar(self, valor, senha):
        if senha == self.__senha:
            self.__saldo -= valor
        else:
            print('Senha invalida')


# cria objeto conta
conta = ContaBancaria(123, 'Francisco', 123456)

print('Numero da conta: ', conta.numero)
print('Titular da Conta: ', conta.titular)

# realiza um deposito
valor = float(input('Valor deposito:'))
senha = int(input('Senha: '))
conta.depositar(valor, senha)

# saldo
print('Saldo: ', conta.get_saldo(senha))

# realiza um saque
valor = float(input('Valor do saque :'))
senha = int(input('Senha: '))
conta.sacar(valor, senha)

# saldo
print('Saldo: ', conta.get_saldo(senha))