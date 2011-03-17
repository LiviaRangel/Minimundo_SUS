class Internacao:
    internacoes = []
    def __init__(self, codigo, data_inicio, data_fim, medico):
        #def __init__(self, codigo, data_inicio, data_fim, medico, paciente, hospital):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.medico = medico
        self.paciente = None
        self.vincular_internacao()
	#self.hospital = hospital
	#self.gravarInternacao(self)
    def vincular_internacao(self):
        Internacao.internacoes.append(self)

