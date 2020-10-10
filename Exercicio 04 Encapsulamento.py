"""
Implemente a classe CarroCorrida

Classe CarroCorrida

Atributos (todos privados):
numero: número de identificação do carro 
piloto: nome do piloto do carro ao carro
velocidade_maxima: velocidade máxima do carro em km/h 
velocidade_atual: velocidade atual do carro em km/h (valor inicial deve ser zero)
ligado: informa se o carro está ligado (valor inicial deve ser False)


Métodos:
ligar: define o carro como ligado
desligar: define o carro como desligado
acelerar: aumenta velocidade atual do carro em N km/h. O carro só pode acelerar se estiver ligado. Ao acelerar, o carro nunca pode ultrapassar a sua velocidade máxima
frear: define a velocidade atual do carro em 0 km/h. 
Criar os métodos get e set, quando for necessário.


Utilize o trecho de programa abaixo para testar a sua classe
carro = CarroCorrida(1, "Paulo", 150)
carro.acelerar(20)
print(carro.get_velocidade_atual())         # imprime 0, porque o carro está desligado
carro.ligar()
carro.acelerar(20)                          
print(carro.get_velocidade_atual())         # imprime 20
carro.acelerar(80)
print(carro.get_velocidade_atual())         # imprime 100
carro.acelerar(70)
print(carro.get_velocidade_atual())         # imprime 150, não ultrapassar a vel. max.
carro.frear()
print(carro.get_velocidade_atual())         # imprime 0
"""
class CarroCorrida:
    def __init__(self, numero, piloto, velocidade_maxima):
        self.__numero = numero
        self.__piloto = piloto
        self.__velocidade_maxima = velocidade_maxima
        self.__velocidade_atual = 0
        self.__ligado = False

    def ligar(self):
        self.__ligado = True

    def desligar(self):
        self.__ligado = False

    def acelerar(self, velocidade):
        if self.__ligado is True:
            self.__velocidade_atual += velocidade
            # se ultrapassar a velocidade máxima, mantém a velocidade limitada na máxima
            if self.__velocidade_atual > self.__velocidade_maxima:
                self.__velocidade_atual = self.__velocidade_maxima

    def frear(self):
        self.__velocidade_atual = 0

    def get_velocidade_atual(self):
        return self.__velocidade_atual


carro = CarroCorrida(1, "Paulo", 150)
carro.acelerar(20)
print(carro.get_velocidade_atual())         # imprime 0, porque o carro esta desligado
carro.ligar()
carro.acelerar(20)
print(carro.get_velocidade_atual())         # imprime 20
carro.acelerar(80)
print(carro.get_velocidade_atual())         # imprime 100
carro.acelerar(70)
print(carro.get_velocidade_atual())         # imprime 150, não ultrapassar a vel. max.
carro.frear()
print(carro.get_velocidade_atual())         # imprime 0