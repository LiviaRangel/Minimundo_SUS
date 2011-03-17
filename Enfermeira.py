from Empregado import *

class Enfermeira(Empregado):
    enfermeiras = []
    def __init__(self, nome, matricula, cargo):
        Empregado.__init__(self, nome, matricula)
        self.cargo = cargo
        self.vincular_enfermeira()

    def vincular_enfermeira(self):
        Enfermeira.enfermeiras.append(self)

