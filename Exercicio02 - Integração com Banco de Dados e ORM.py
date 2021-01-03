"""
Implementar um programa em Python que realize as seguintes operações:

Conectar com o banco de dados SQLITE e criar as tabelas AUTOR e LIVRO (utilize os scripts abaixo para a criação das tabelas).

CREATE TABLE IF NOT EXISTS AUTOR (
ID int not null,
NOME varchar(255) not null)

CREATE TABLE IF NOT EXISTS LIVRO (
ID int not null,
TITULO VARCHAR(255) NOT NULL,
PAGINAS INT NOT NULL,
AUTOR_ID INT not null)

Criar as classes Autor e Livro e fazer o mapeamento das tabelas.
Inserir na tabela dois autores e dois livros.
Fazer uma consulta para verificar se os dados foram inseridos corretamente. 

"""

import sqlalchemy

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE
# caso o arquivo não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///exercicio2.db")
connection = engine.connect()


# Cria uma Sessão com o banco de dados
Base = declarative_base(engine)
session = Session()


connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR (
                    ID int not null,
                    NOME varchar(255) not null)
                    """)

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO (
                        ID int not null,
                        TITULO VARCHAR(255) NOT NULL,
                        PAGINAS INT NOT NULL,
                        AUTOR_ID INT not null)
                        """)


class Autor(Base):
    __tablename__ = 'Autor'
    id = Column('ID', Integer, primary_key=True, autoincrement=False)
    nome = Column('NOME', String(255))

    def __init__(self, id, nome):
        self.id = id
        self.nome = nome


class Livro(Base):
    __tablename__ = "LIVRO"
    id = Column('ID', Integer, primary_key=True, autoincrement=False)
    titulo = Column('TITULO', String(255))
    paginas = Column('PAGINAS', Integer)
    autor_id = Column('AUTOR_ID', Integer)

    def __init__(self, id, titulo, paginas, autor_id):
        self.id = id
        self.titulo = titulo
        self.paginas = paginas
        self.autor_id = autor_id


autor1 = Autor(1, 'Paulo')
autor2 = Autor(2, 'Maria')

lista = [autor1, autor2]
session.add_all(lista)
session.commit()


livro1 = Livro(1, 'Titulo do livro 1', 300, autor1.id)
livro2 = Livro(2, 'Titulo do livro 2', 150, autor2.id)

lista = [livro1, livro2]
session.add_all(lista)
session.commit()

resultado = session.query(Autor).all()
for r in resultado:
    print(r.id, r.nome)

resultado = session.query(Livro).all()
for r in resultado:
    print(r.id, r.titulo, r.paginas, session.query(Autor).get(r.autor_id).nome)
