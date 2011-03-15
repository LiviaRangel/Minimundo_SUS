from Empregado import *

class Enfermeira(Empregado):
    def __init__(self, nome, matricula, cargo):
        Empregado.__init__(self, nome, matricula)
        self.cargo = cargo

    def vincular_enfermeira_hospital(self, hospital):
        pass

