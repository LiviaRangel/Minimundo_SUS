class Hospital:
    def __init__(self, nome, codigo, endereco):
        self.nome = nome
        self.codigo = codigo
        self.endereco = endereco
        self.internacoes = []
        self.empregados = []

    def vincular_internacao_hospital(self, internacao):
        self.internacoes.append(internacao)

    def vincular_empregado_hospital(self, empregado):
        self.empregados.append(empregado)

