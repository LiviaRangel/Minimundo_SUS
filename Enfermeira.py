from Empregado import *

class Enfermeira(Empregado):
    def __init__(self, nome, matricula, cargo):
        Empregado.__init__(self, nome, matricula)
        self.cargo = cargo

