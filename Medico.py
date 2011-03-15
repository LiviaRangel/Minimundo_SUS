from Empregado import *

class Medico(Empregado):
    def __init__(self, nome, matricula, especialidade):
        Empregado.__init__(self, nome, matricula)
        self.especialidade = especialidade

    def vincular_medico_hospital(self, hospital):
        pass
        #raise RuntimeError('lerolero')
        #print hospital
        #self.hospitais.append(hospital)

