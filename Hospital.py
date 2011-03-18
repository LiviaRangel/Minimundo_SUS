class Hospital:
    hospitais = []
    def __init__(self, nome, codigo, endereco):
        self.nome = nome
        self.codigo = codigo
        self.endereco = endereco
        self.internacoes = []
        self.empregados = []
        self.vincular_hospital()

    def vincular_hospital(self):
        Hospital.hospitais.append(self)

    def vincular_internacao_hospital(self, internacao):
        if internacao not in self.internacoes:
            self.internacoes.append(internacao)

    def vincular_empregado_hospital(self, empregado):
        self.empregados.append(empregado)

