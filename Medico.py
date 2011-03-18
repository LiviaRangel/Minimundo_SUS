from Empregado import *

class Medico(Empregado):
    medicos = []
    def __init__(self, nome, matricula, especialidade):
        Empregado.__init__(self, nome, matricula)
        self.especialidade = especialidade
        self.internacoes = []
        self.vincular_medico()

    def vincular_medico(self):
        Medico.medicos.append(self)

    def vincular_internacao(self, internacao):
        self.internacoes.append(internacao)
