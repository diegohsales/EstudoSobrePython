# Exemplo 1:
# Criar dicionario para armazenar um cadastro de pessoas
# Armazenar CPF e NOME
cadastro = {123456: "Paulo",
            5678890: "Maria",
            345434: "Pedro"}

print(cadastro)
print(cadastro[123456])

# Adicionar os dados de uma pessoa
cadastro[9999999] = "João"
print(cadastro) 

# Alterar o Nome de uma pessoa
cadastro[9999999] = "João Paulo"
print(cadastro)

# Solicitar os dados de 3 pessoas e adicionar ao dicionário
'''cadastro = {}
for a in range(3):
    cpf = int(input("CPF: "))
    nome = input("Nome: ")
    cadastro[cpf] = nome
print(cadastro)
'''

for a in cadastro:
    if a == 9999999:
        print("CPF:", a, "Nome:", cadastro[a])

# Excluir os dados de uma pessoa
cadastro.pop(9999999)
print(cadastro)

# Verificar se chave existe no dicionário
if 333333 in cadastro:
    cadastro.pop(333333)
else:
    print("A chave não existe")
print(cadastro)


# Exemplo 2:
# Criar dicionario para armazenar uma lista de 5 notas
notas = {"Maria": [10,9,8,7,6],
         "João": [5,7,8,9,10]}

# Exibir notas de um aluno específico
print(notas["Maria"])

# Inserir uma nova nota a um aluno especifico
notas["João"].append(9.5)
print(notas)


produtos = {}
for a in range(5):
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    produtos[nome] = preco
    
print(produtos)

print("Produtos com valor superior a 50.00: ")
for a in produtos:
    if produtos[a] > 50:
        print(a)

        

alunos = {}

'''
for a in range(5):
    nome = input("Nome: ")
    n1 = float(input("Nota: "))
    n2 = float(input("Nota: "))
    n3 = float(input("Nota: "))
    lista = [n1, n2, n3]  
    alunos[nome] = lista
'''
for a in range(5):
    nome = input("Nome: ")
    lista = []
    for i in range(3):                  # preenche lista com as notas
        nota = float(input("Nota: "))
        lista.append(nota)
    alunos[nome] = lista
    
print(alunos)

for a in alunos:
    lista = alunos[a]           # acessa a lista de notas
    media = sum(lista) / len(lista)
    print("Nome:", a, " - Media:", media)
