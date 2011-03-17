class Atendimento:
    atendimentos = []
    def __init__(self):
        self.empregado = None
        self.internacao = None
        self.vincular_atendimento()

    def vincular_atendimento(self):
        Atendimento.atendimentos.append(self)

