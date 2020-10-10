"""
Crie a classe Imovel, que possui um endereço e um preço.
Crie uma classe Novo, que herda de Imovel e possui um adicional no preço.
Crie uma classe Velho, que herda de Imovel e possui um desconto no preço.
O método calcular_preco das classes Novo e Velho deve retornar o preço atualizado de acordo com o adicional ou desconto. 
"""







imovel = Imovel("Rua Silva, 123", 300000.0)
imovel_novo = Novo("Rua Joaquim, 999", 250000.0, 20000.0)
imovel_velho = Velho("Av. Brasil, 777", 500000.0, 35000.0)
