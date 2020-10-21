"""
Crie uma hierarquia de classes para representar os diferentes tipos de funcionários de um escritório que tem os 
seguintes cargos: gerente, assistente e vendedor. 
Escreva uma classe base abstrata chamada Funcionario que declara um método abstrato calcular_salario()
Essa classe também deve definir os seguintes atributos: nome, matricula e salario_base.
Essa classe abstrata deverá ser herdada pelas outras classes que são: Gerente, Assistente e Vendedor. 
Em cada classe filha deve-se sobrescrever o método calcular_salario(). Este método deve calcular e retornar o 
salário de cada funcionário, da seguinte forma: 
O gerente recebe duas vezes o salário_base.
O assistente recebe o salário_base.
O vendedor recebe o salário_base mais uma comissão de 10%. 
Implemente um programa principal que cria um objeto de cada tipo (gerente, assistente e vendedor) e os armazena 
em uma lista Percorra essa lista e imprima o salário de cada funcionário.
"""