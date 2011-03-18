class Atendimento:
    atendimentos = []
    def __init__(self, empregado, internacao):
        self.empregado = self.vincular_empregado(empregado)
        self.internacao = self.vincular_atendimento_internacao(internacao)
        self.vincular_atendimento()

    def vincular_atendimento(self):
        Atendimento.atendimentos.append(self)

    def vincular_atendimento_internacao(self, internacao):
        if self not in internacao.atendimentos:
            internacao.vincular_atendimento(internacao)
        return internacao
        
    def vincular_empregado(self, empregado):
        if self not in empregado.atendimentos:
            empregado.vincular_atendimento(self)
        return empregado
