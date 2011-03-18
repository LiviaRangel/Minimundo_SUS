class Atendimento:
    atendimentos = []
    def __init__(self, internacao):
        self.empregado = None
        self.internacao = self.vincular_atendimento_internacao(internacao)
        self.vincular_atendimento()

    def vincular_atendimento(self):
        Atendimento.atendimentos.append(self)

    def vincular_atendimento_internacao(self, internacao):
        if self not in internacao.atendimentos:
            internacao.vincular_atendimento(internacao)
        return internacao
