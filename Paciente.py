class Paciente:
    pacientes = []
    def __init__(self, nome, codigo_seguro_social, idade):
        self.nome = nome
        self.codigo_seguro_social = codigo_seguro_social
        self.idade = idade
        self.internacoes = []
        self.vincular_paciente()

    def vincular_paciente(self):
        Paciente.pacientes.append(self)

