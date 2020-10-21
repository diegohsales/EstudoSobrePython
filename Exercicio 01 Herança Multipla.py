"""
Uma universidade necessita de um sistema que facilite a sua gestão acadêmica. Implemente as classes de modo que obedeçam os 
relacionamentos apresentados no diagrama abaixo:


Sabe-se que um professor é um funcionário. Além de professores, há funcionários que são técnicos administrativos. 
Para cada funcionário, independente de ser professor ou técnico, é necessário saber seu nome, endereço, telefone, cpf e salário. 
Especificamente para professores, é necessário saber sua titulação e as disciplinas que ele leciona.
Especificamente para técnicos administrativos, é necessário saber seu cargo.
Para cada aluno é necessário saber seu nome, endereco, telefone, cpf e as disciplinas que ele cursa.
Para cada disciplina é necessário registrar seu nome.
"""
















disciplina1 = Disciplina("Programação")
disciplina2 = Disciplina("Banco de Dados")
professor1 = Professor("Joao", "Rua Silva, 456", "(11)99999-9555", "9999999", 2000, "Mestrado")

aluno1 = Aluno("Maria", "Avenida São Francisco, 239", "(11)98888-8435", "555555")
tecnico1 = Tecnico("Pedro", "Rua Rocha, 77", "(11)93333-3333", "8787887", 1500, "Tecnico")

aluno1.incluir_disciplina(disciplina1)
aluno1.incluir_disciplina(disciplina2)
professor1.incluir_disciplina(disciplina1)
