"""
Observe o diagrama de classes abaixo e implemente as classes Carro e Pneu. O diagrama representa uma associação onde 
um Carro possui quatro Pneus.

Classe Carro:
Atributos:
ligado: valor booleano que indica se o carro está ligado ou desligado (deve iniciar com o valor False)
pneu1, pneu2, pneu3, pneu4: objetos do tipo Pneu que representa cada um dos pneus do carro (devem receber os valores 
iniciais no construtor).
Métodos:
ligar: altera o valor do atributo ligado para True
desligar: altera o valor do atributo ligado para False
verificar_pneu: se o carro estiver ligado, esse método deve exibir a pressão de cada um dos pneus. Se o carro estiver 
desligado, o método deve exibir a mensagem ‘Carro Desligado'

Classe Pneu:
Atributos:
pressao: valor inteiro que indica a pressão de ar do pneu (inicializado no construtor)
Métodos:
furar(): simula um pneu furado, alterando o valor do atributo pressao para zero.

Você pode utilizar o trecho de programa abaixo para testar as suas classes.

p1 = Pneu(32)
p2 = Pneu(32)
p3 = Pneu(36)
p4 = Pneu(36)
meucarro = Carro(p1, p2, p3, p4)
meucarro.ligar()
meucarro.pneu3.furar()
meucarro.verificar_pneu()        # Deve exibir a pressão de cada pneu.
meucarro.desligar()
meucarro.verificar_pneu()        # Deve exibir mensagem que o carro está desligado
"""
class Pneu:
    def __init__(self, pressao):
        self.pressao = pressao

    def furar(self):
        self.pressao = 0


class Carro:
    def __init__(self, pneu1, pneu2, pneu3, pneu4):
        self.ligado = False
        self.pneu1 = pneu1
        self.pneu2 = pneu2
        self.pneu3 = pneu3
        self.pneu4 = pneu4

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def verificar_pneu(self):
        if self.ligado is True:
            print("Pressão do pneu 1: ", self.pneu1.pressao)
            print("Pressão do pneu 2: ", self.pneu2.pressao)
            print("Pressão do pneu 3: ", self.pneu3.pressao)
            print("Pressão do pneu 4: ", self.pneu4.pressao)
        else:
            print("O carro está desligado")


p1 = Pneu(32)
p2 = Pneu(32)
p3 = Pneu(36)
p4 = Pneu(36)
meucarro = Carro(p1, p2, p3, p4)
meucarro.ligar()
meucarro.pneu3.furar()
meucarro.verificar_pneu()       # exibir a pressão de cada pneu.
meucarro.desligar()
meucarro.verificar_pneu()       # exibir mensagem que o carro está desligado