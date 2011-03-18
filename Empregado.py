class Empregado:
    empregados = []
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.hospitais = []
        self.atendimentos = []
        self.vincular_empregado()

    def vincular_empregado(self):
        Empregado.empregados.append(self)

    def vincular_empregado_hospital(self, hospital):
        #pass
        if (len(self.hospitais) == 3):
            raise RuntimeError("O empregado ja esta vinculado a 3 hospitais.")
        elif (hospital in self.hospitais):
            raise RuntimeError("Nao se admite um empregado com mais de um vinculo em um mesmo hospital.")
        else:
        #print hospital
            self.hospitais.append(hospital)

    def vincular_empregado_atendimento(self, atendimento):
        self.atendimentos.append(atendimento)

    @staticmethod
    def relatorio_empregados_hospital(cod_hospital):
        resultado = []
        if len(Empregado.empregados) == 0:
	    resultado = "Nao ha empregados cadastrados."
  	for i in range(len(Empregado.empregados)):
            resultado += "\n*** Empregados *** "
	    if Empregado.empregados[i].hospital.codigo == cod_hospital:
	        resultado += "\nMatricula: ",Empregado.empregados[i].matricula
	        resultado += "\nNome: ", Empregado.empregados[i].nome      
	        resultado += "----------------"
	    else:
	        resultado = "Nao ha empregados vinculados a esse hospital."
	    resultado += "\n*****   FIM   ***** "
	return resultado

