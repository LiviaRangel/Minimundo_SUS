from Hospital import *
from Medico import *
from Enfermeira import *
from Paciente import *
from Internacao import *
from Atendimento import *

option = 0
opt = 0
opr = 0

while option != 5:
    print "==== Bem-vindo ao SUS ===="
    print "1 - Cadastros"
    print "2 - Internacao"
    print "3 - Atendimento"
    print "4 - Relatorios"
    print "5 - Sair"
    option = input()

#### 1 - CADASTROS ####
    if option == 1:
        while opt != 5:
            print "====== Cadastrar ======"
            print "1 - Hospital"
            print "2 - Medico"
            print "3 - Enfermeira"
            print "4 - Paciente"
            print "5 - Voltar"
            opt = input()

	    if opt == 1:
                print "--- Hospital --- "
                print "Digite o codigo: "
                codigo = raw_input()
                print "Digite o nome: "
                nome = raw_input()
                print "Digite o endereco: "
                endereco = raw_input()
                Hospital(nome, codigo, endereco)

	    if opt == 2:
                print "--- Medico --- "
                print "Digite a matricula: "
                matricula = raw_input()
                print "Digite o nome: "
                nome = raw_input()
                print "Digite a especialidade: "
                especialidade = raw_input()    
                Medico(nome, matricula, especialidade)

	    if opt == 3:
                print "--- Enfermeira --- "
                print "Digite a matricula: "
                matricula = raw_input()
                print "Digite o nome: "
                nome = raw_input()
                print "Digite o cargo: "
                cargo = raw_input()    
                Enfermeira(nome, matricula, cargo)

	    if opt == 4:
                print "--- Paciente --- "
                print "Digite o seguro social: "
                seguro = raw_input()
                print "Digite o nome: "
                nome = raw_input()
                print "Digite o idade: "
                idade = raw_input()    
                Enfermeira(nome, seguro, idade)
	

#### 2 - INTERNACAO ####
    if option == 2:
        while opt != 3:
            print "====== Internacao ======"
            print "1 - Inserir"
            print "2 - Fechar internacao"
            print "3 - Voltar"
            opt = input()

	    if opt == 1:
	        print "++++ Internacao ++++"
                print "Digite o codigo: "
                codigo = raw_input()
                print "Digite a data de inicio: "
                data_inicio = raw_input()
                print "Digite o seguro social do paciente: "
                paciente = raw_input()
                print "Digite a matricula do medico: "
                medico = raw_input()
                print "Informe o codigo do Hospital: "
                cod_hospital = raw_input()
		for i in range(len(Hospital.hospitais)):
   	            if Hospital.hospitais[i].codigo == cod_hospital:
			hospital = Hospital.hospitais[i]
	            else:
			print "Hospital nao cadastrado, a internacao nao pode ser feita."
                Internacao(codigo, data_inicio, medico, paciente, hospital)

	    if opt == 2:
                print "++++ Internacao ++++"
                print "Digite o codigo: "
                codigo = raw_input()
                print "Informe a data fim: "
                data_fim = raw_input()
                FecharInternacao(codigo, data_fim)

#### 3 - ATENDIMENTO ####
    if option == 3:
	print "++++ Atendimento ++++"
        print "Informe a internacao: "
        internacao = raw_input()
        print "Informe a matricula do responsavel pelo atendimento: "
        responsavel = raw_input()
        Atendimento(internacao, responsavel)

#### 4 - RELATORIOS ####
    if option == 4:
        while opr != 5:
            print "====== Relatorios ======"
            print "1 - Internacoes por Hospital"
            print "2 - Profissionais por Hospital"
            print "3 - Atendimentos por internacao"
            print "4 - Hospitais por profissionais"
            print "5 - Voltar"
            opr = input()

	    if opr == 1:
                print "*** Internacoes por Hospital *** "
	        print "* Informe o hospital: "
	        cod_hospital = raw_input()
                print Internacao.relatorio_pacientes_internados_hospital_com_medicos_e_periodo(cod_hospital)

	    if opr == 2:
                print "*** Profissionais por Hospital *** "
	        print "* Informe o hospital: "
	        internacao = raw_input()

	    if opr == 3:
                print "*** Atendimentos por internacao *** "
	        print "* Informe a internacao: "
	        internacao = raw_input()


	    if opr == 4:
                print "*** Hospitais por profissionais*** "
	        print "* Informe a matricula do profissional: "
	        internacao = raw_input()



