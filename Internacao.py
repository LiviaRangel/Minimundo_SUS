class Internacao:
    internacoes = []
    def __init__(self, codigo, data_inicio, medico, paciente, hospital):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = None
        self.medico = medico
        self.paciente = paciente
        self.hospital = self.vincular_internacao_hospital(hospital)
        self.atendimentos = []
        self.vincular_internacao()

    def vincular_internacao(self):
        Internacao.internacoes.append(self)

    def vincular_internacao_hospital(self, hospital):
        if self not in hospital.internacoes:
            hospital.vincular_internacao_hospital(self)            
        return hospital
        
    def vincular_atendimento(self, atendimento):
        if atendimento not in self.atendimentos:
            self.atendimentos.append(atendimento)
        
