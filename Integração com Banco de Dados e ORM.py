"""
ORM (Object-Relational Mapping)

    • Object-Relational Mapping (ORM), em português,
mapeamento objeto-relacional, é uma técnica para
aproximar o paradigma de programação orientada a
objetos ao paradigma do banco de dados relacional

    • Ultimamente tem sido muito utilizada e vem crescendo
bastante nos últimos anos:
    – Permite abstrair o código de SQL
    – Aproxima o paradigma de POO ao paradigma de
banco de dados relacional
    – Aumenta a produtividade

    • O uso da técnica de ORM é realizado através de um
mapeador objeto-relacional, que geralmente é uma
biblioteca ou framework que ajuda no mapeamento e uso
do banco de dados
    – Utilizaremos o framework SQLAlchemy
    
    • Essa técnica facilita a manipulação, inserção e atualização
dos dados contidos na tabela.

    • O ORM representa as tabelas do banco de dados em classes:
    – Campos da tabela são representados pelos atributos da classe
    – Cada registro é representado na forma de um objeto

    • SQLAlchemy é um framework python usado para interagir
com uma grande variedade de bancos de dados.
    – https://docs.sqlalchemy.org/en/13/orm/
    
    • Ele permite que você crie modelos e consultas de uma
maneira mais próxima ao paradigma de orientação a
objetos.

Referências
• SQLAlchemy ORM Documentation
– https://docs.sqlalchemy.org/en/13/orm/
• Essential SQLAlchemy
– https://bit.ly/35JaQ5i


Consultar dados da tabela
Funções Principais:
.query(nome_da_classe) : executa uma query na tabela mapeada pela classe informada no parâmetro.
.all() : retorna todos os resultados da consulta realizada
.first() : retorna o primeiro resultado da consulta realizada
.get(valor) : realiza a busca por um registro específico, de acordo com o valor informado (primary_key)
.filter() : define o filtro a ser aplicado na consulta
.order_by() : ordena a consulta relaizada de acordo com o valor informado



Conectando com o SQL SERVER
# Importar os módulos:
import pyodbc
import sqlalchemy

# Criar conexão com SQL SERVER
engine = sqlalchemy.create_engine("mssql+pyodbc://<username>:<password>@<dsnname>?driver=SQL+Server")
connection = engine.connect()
https://docs.sqlalchemy.org/en/13/dialects/mssql.html
"""