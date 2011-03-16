class Internacao:

    Internacoes = []
    def __init__(self, codigo, data_inicio, data_fim, medico):
        #def __init__(self, codigo, data_inicio, data_fim, medico, paciente, hospital):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.medico = medico
	#self.hospital = hospital
	#self.gravarInternacao(self)

    def gravarInternacao(self, internacao):
        self.Internacoes.append(internacao)


class FecharInternacao:
    def __init__(self, codigo, data_fim):
	pass

