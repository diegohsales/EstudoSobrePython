'''
Classe Cachorro
- Atributos: nome, idade
- Métodos: andar, comer, latir
'''


class Cachorro:
    # construtor (utilizado para definir os atributos da classe)
    def __init__(self, nome, idade):
        # atributos
        self.nome = nome
        self.idade = idade

    # metodos
    def andar(self, distancia):
        print("O cachorro andou", distancia, "metros")

    def comer(self):
        print("O cachorro de nome", self.nome, "comeu")

    def latir(self):
        print("O cachorro latiu")


# cria uma instancia (objeto) da classe Cachorro
dog = Cachorro("Rex", 4)
print("O cachorro " + dog.nome + " possui " + str(dog.idade) + " anos")
dog.andar(10)
dog.comer()
dog.latir()

# cria outra instancia (objeto) da classe Cachorro
meu_cachorro = Cachorro("Snoopy", 2)
print("O cachorro " + dog.nome + " possui " + str(dog.idade) + " anos")
meu_cachorro.andar(5)
meu_cachorro.latir()
# altera a idade do cachorro
meu_cachorro.idade = 3
print("O cachorro " + dog.nome + " possui " + str(dog.idade) + " anos")

'''
Criar uma classe Pessoa.
- Atributos: nome, email, telefone.
- Métodos: Um método deve exibir os dados desta pessoa.
'''


class Pessoa:
    def __init__(self, nome, email, telefone):             # construtor
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir(self):
        print('Nome:', self.nome)
        print('Email: ', self.email)
        print('Telefone: ', self.telefone)


paulo = Pessoa('Paulo Vieira', 'paulo@email.com', 1199999999)
paulo.exibir()

pessoa1 = Pessoa('Maria', 'maria@email.com', 9999999)
pessoa1.exibir()
pessoa1.nome = 'Maria Paula'
print('Nome: ', pessoa1.nome)


'''
Criar uma classe Aluno
- Atributos: ra, nome, email, lista de notas.
- Métodos: inserir_nota, calcular_media
'''


class Aluno:
    def __init__(self, ra, nome, email):            # construtor
        self.ra = ra
        self.nome = nome
        self.email = email
        self.notas = []

    def inserir_nota(self, nota):
        self.notas.append(nota)

    def definir_notas(self, lista):
        self.notas = lista

    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)
        return media


aluno1 = Aluno(1111111, 'João', 'joao@email.com')
aluno2 = Aluno(2222222, 'Maria Paula', 'maria@email.com')
aluno3 = Aluno(3333333, 'Pedro', 'pedro@email.com')

aluno1.inserir_nota(10)
aluno1.inserir_nota(8)
print('Média: ', aluno1.calcular_media())

aluno2.inserir_nota(7)
aluno2.inserir_nota(5)
aluno2.inserir_nota(8)
print('Média: ', aluno2.calcular_media())

aluno3.definir_notas([10, 6, 7, 9, 5])
print('Média:', aluno3.calcular_media())