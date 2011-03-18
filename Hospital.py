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

    @staticmethod
    def relatorio_hospital_empregados(prof):
        resultado = []
        if len(Hospital.hospitais) == 0:
	    resultado = "Nao ha hospitais cadastrados."
  	for i in range(len(Hospital.hospitais)):
            resultado += "\n*** Hospitais *** "
	    if Hospital.hospitais[i].empregados.matricula == prof:
	        resultado += "\nMatricula: ",Hospital.hospitais[i].codigo
	        resultado += "\nNome: ", Hospital.hospitais[i].nome      
	        resultado += "\nEndereco: ", Hospital.hospitais[i].endereco      
	        resultado += "----------------"
	    else:
	        resultado = "Nao ha hospitas vinculados a esse empregado."
	    resultado += "\n*****   FIM   ***** "
	return resultado

