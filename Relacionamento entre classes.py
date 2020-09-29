'''

Exemplo de Associação de Classes:

|-------------------|           |-------------------|
| Pessoa            |           | Endereco          |
|-------------------|           |-------------------|
| nome              |           | rua               |
| idade             |-----------| numero            |
| sexo              |           | complemento       |
| endereco          |           | cep               |
|-------------------|           |-------------------|
| exibir_dados()    |           | exibir_dados()    |
|-------------------|           |-------------------|

'''


class Endereco:
    def __init__(self, rua, numero, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = ""
        self.cep = cep

    def exibir_dados(self):
        print("Rua: ", self.rua)
        print("Numero: ", self.numero)
        print("Complemento: ", self.complemento)
        print("CEP: ", self.cep)


class Pessoa:
    def __init__(self, nome, idade, sexo, endereco):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def exibir_dados(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Sexo: ", self.sexo)
        print("Endereço: ")
        # Executa metodo exibir_dados da Classe Endereço
        self.endereco.exibir_dados()


# Cria objeto Endereco
end = Endereco("Av. Paulista", 100, 999999999)
# Cria objeto Pessoa e associa o objeto Endereco a ela
pessoa1 = Pessoa("Paulo", 25, "M", end)
pessoa1.exibir_dados()

# Cria outro objeto Endereco
end2 = Endereco("Av. Brasil", 198, 777777777)
# Cria outro objeto Pessoa
pessoa2 = Pessoa("Maria", 30, "F", end2)
pessoa2.exibir_dados()

'''
|-------------------|           |-------------------|
| Cachorro          |           | Pessoa            |
|-------------------|           |-------------------|
| nome              |           | nome              |
| idade             |-----------| sobrenome         |
| proprietario      |           |                   |
|-------------------|           |-------------------|
|                   |           |                   |
|-------------------|           |-------------------|
'''


class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


class Cachorro:
    def __init__(self, nome, idade, proprietario):
        self.nome = nome
        self.idade = idade
        self.proprietario = proprietario


pessoa1 = Pessoa('Paulo', 'Vieira')
dog = Cachorro('Rex', 2, pessoa1)
print(dog.nome)
print(dog.proprietario.nome, dog.proprietario.sobrenome)


'''
|------------|         |---------------------|        |-------------|
| Produto    |         | Carrinho            |        | Cliente     |
|------------|         |---------------------|        |-------------|
| descricao  |0..*    1| cliente             |1      1| nome        |
| valor      |---------| produtos            |--------|-------------|
|------------|         |---------------------|        |             |
|            |         | adicionar_produto() |        |-------------|
|------------|         | listar_produtos()   |
                       | calcular_total()    |
                       |---------------------|
'''


class Cliente:
    def __init__(self, nome):
        self.nome = nome


class Produto:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor


class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente      # armamzena um objeto da classe Cliente
        self.produtos = []    # armazena uma lista de objetos da classe Produto

    def adicionar_produto(self, prod):
        self.produtos.append(prod)

    def listar_produtos(self):
        for prod in self.produtos:
            print(prod.descricao, prod.valor)

    def calcular_total(self):
        soma = 0
        for prod in self.produtos:
            soma += prod.valor
        return soma


# cria objetos Produto
prod1 = Produto("HD Externo", 100.0)
prod2 = Produto("Pen Drive", 20.0)
prod3 = Produto("Teclado", 45.0)

# cria objeto Cliente
cliente1 = Cliente("Paulo")

# cria objeto Carrinho de Compra
carrinho1 = Carrinho(cliente1)

# insere produtos no carrinho
carrinho1.adicionar_produto(prod1)
carrinho1.adicionar_produto(prod2)
carrinho1.adicionar_produto(prod2)
carrinho1.adicionar_produto(prod3)

# lista produtos do carrinho
carrinho1.listar_produtos()

# exibe total da compra
print('Total: ', carrinho1.calcular_total())