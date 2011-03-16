from Empregado import *

class Medico(Empregado):
    def __init__(self, nome, matricula, especialidade):
        Empregado.__init__(self, nome, matricula)
        self.especialidade = especialidade

