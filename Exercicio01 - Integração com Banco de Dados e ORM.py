"""
Exercício 1

Implementar um programa em Python que realize as seguintes operações:

Conectar com o banco de dados SQLITE e criar a tabela FUNCIONARIO (utilize o script abaixo para a criação da tabela)

CREATE TABLE IF NOT EXISTS FUNCIONARIO (
ID INTEGER PRIMARY KEY,
NOME VARCHAR(255) NOT NULL,
IDADE INT NOT NULL,
SALARIO FLOAT NOT NULL)

Criar a classe Funcionario e mapear a tabela criada anteriormente.
Criar 3 objetos da classe Funcionario.
Inserir os dados dos objetos na tabela. 
Realizar uma consulta na tabela de funcionários e verificar se os dados foram inseridos corretamente.
Realizar uma consulta na tabela de todos os funcionários com salário superior a R$ 1500,00.

"""

import sqlalchemy

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE
# caso o arquivo não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///abonodefalta.db")
connection = engine.connect()


# Cria uma Sessão com o banco de dados
Base = declarative_base(engine)
session = Session()


connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255) NOT NULL,
                        IDADE INT NOT NULL,
                        SALARIO FLOAT NOT NULL)
                    """)


class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


lista_funcionarios = []
for i in range(3):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    salario = float(input('Salario: '))
    func = Funcionario(nome, idade, salario)
    lista_funcionarios.append(func)

session.add_all(lista_funcionarios)
session.commit()

print('--------------------------')
lista = session.query(Funcionario).all()
for func in lista:
    print(func.id, func.nome, func.idade, func.salario)

print('--------------------------')
lista = session.query(Funcionario).filter(Funcionario.salario > 1500).all()
for func in lista:
    print(f'ID: {func.id}; Nome: {func.nome}; Idade: {func.idade}; Salario: {func.salario}')