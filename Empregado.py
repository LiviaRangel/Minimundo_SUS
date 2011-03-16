class Empregado:

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.hospitais = []
        self.atendimentos = []

    def vincular_empregado_hospital(self, hospital):
        #pass
        if (len(self.hospitais) == 3):
            raise RuntimeError("O empregado ja esta vinculado a 3 hospitais.")
        elif (hospital in self.hospitais):
            raise RuntimeError("Nao se admite um empregado com mais de um vinculo em um mesmo hospital.")
        #print hospital
        #self.hospitais.append(hospital)

