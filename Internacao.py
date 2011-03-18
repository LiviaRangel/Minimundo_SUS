from Medico import *
from Paciente import *
from Atendimento import *

class Internacao:
    internacoes = []

    def __init__(self, codigo, data_inicio, medico, paciente, hospital):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = None
        self.medico = medico
        self.paciente = self.vincular_paciente(paciente)
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
        
    def vincular_paciente(self, paciente):
        if self not in paciente.internacoes:
            paciente.vincular_internacao(self)            
        return paciente
        
    def vincular_medico(self, medico):
        if self not in medico.internacoes:
            medico.vincular_internacao(self)
        return medico

    @staticmethod
    def relatorio_pacientes_internados_hospital_com_medicos_e_periodo(cod_hospital):
        resultado = []
        if len(Internacao.internacoes) == 0:
	    resultado = "Nao ha internacoes cadastradas."
  	for i in range(len(Internacao.internacoes)):
            resultado += "\n*** Internacoes *** "
	    if Internacao.internacoes[i].hospital.codigo == cod_hospital:
	        resultado += "\nData inicio: ",Internacao.internacoes[i].data_inicio
	        resultado += "\nData fim: ", Internacao.internacoes[i].data_fim      
         	for j in range(len(Medico.medicos)):
        	    if Medico.medicos[j].matricula == Internacao.internacoes[i].medico:
        	        resultado += "\nMedico: ",Medico.medicos[j].matricula
        		resultado += "\nNome: ",Medico.medicos[j].nome        
	        for k in range(len(Paciente.pacientes)):
	            if Paciente.pacientes[k].codigo_seguro_social == Internacao.internacoes[i].paciente:
	        	resultado += "\nPaciente: ",Paciente.pacientes[k].codigo_seguro_social
	        	resultado += "\nNome: ",Paciente.pacientes[k].nome
	        	resultado += "\nIdade: ",Paciente.pacientes[k].idade
	        resultado += "----------------"
	    else:
	        resultado = "Nao ha internacao vinculada a esse hospital"
	    resultado += "\n*****   FIM   ***** "
	    return resultado

    @staticmethod
    def relatorio_atendimentos_internacao(internacao):
        resultado = []
        if len(Atendimento.atendimentos) == 0:
	    resultado = "Nao ha atendimentos cadastradas."
  	for i in range(len(Internacao.internacoes)):
            resultado += "\n*** Atendimentos *** "
	    if Internacao.internacoes[i].codigo == internacao:
	        for j in range(len(Internacao.internacoes[i].atendimentos[j])):
        	    resultado += "\nMatricula: ",Internacao.internacoes[i].atendimentos[j].empregado.matricula
        	    resultado += "\nNome: ",Internacao.internacoes[i].atendimentos[j].empregado.nome
	    else:
	        resultado = "Nao ha atendimentos vinculados a essa internacao"
	    resultado += "\n*****   FIM   ***** "
	    return resultado
