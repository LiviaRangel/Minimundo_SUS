import unittest
import Hospital, Paciente, Medico, Enfermeira, Internacao, Atendimento, Empregado


class TesteHospital(unittest.TestCase):

    def setUp(self):
        self.hospital = Hospital.Hospital("Dr.Beda","H001","Rua do Gas")
        self.paciente = Paciente.Paciente("Paciente", "12345", 18)
        self.internacao = Internacao.Internacao("I001","05/02/2011", "M001", self.paciente, self.hospital)
        self.assertIn(self.hospital, Hospital.Hospital.hospitais, "Um hospital deve ser registrado na lista global de hospitais")
        self.assertEqual(self.internacao.hospital, self.hospital)
        
        self.assertIn(self.internacao, self.hospital.internacoes)
        self.assertEqual(len(self.hospital.internacoes), 1)
        
        #relatorio_empregados_hospital = self.hospital.relatorio_hospital_empregados("H001")
        #self.assertIsInstance(relatorio_hospital_empregados, list)

    def testInsertHospital(self):
        self.assertNotEqual(self.hospital.nome, None)
        self.assertNotEqual(self.hospital.codigo, None)
        self.assertNotEqual(self.hospital.endereco, None)

    def testListaHospitais(self):
        self.assertListEqual(self.hospital.empregados, [], "Um hospital deve possuir uma lista de empregados")

    def testListaInternacoes(self):
        self.assertListEqual(self.hospital.internacoes, [self.internacao], "Um hospital deve possuir uma lista de internacoes de pacientes")

    def testVinculoInternacoesHospital(self):
        self.assertEqual(len(self.hospital.internacoes), 1)

    def testVinculoEmpregadoHospital(self):
        self.hospital.vincular_empregado_hospital(1)
        self.assertEqual(len(self.hospital.empregados), 1)

class TestePaciente(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente.Paciente("Jose da Silva","P001","18")
        self.assertIn(self.paciente, Paciente.Paciente.pacientes, "Um paciente deve ser registrado na lista geral de pacientes")

    def testInsertPaciente(self):
        self.assertNotEqual(self.paciente.nome, None)
        self.assertNotEqual(self.paciente.codigo_seguro_social, None)
        self.assertNotEqual(self.paciente.idade, None)

    def testPossuiInternacoes(self):
        self.assertListEqual(self.paciente.internacoes, [], "Um paciente possui uma lista das internacoes que sofreu")


class TesteEmpregado(unittest.TestCase):
    def setUp(self):
        self.empregado = Empregado.Empregado("Dr. House","M001")
        self.assertIn(self.empregado, Empregado.Empregado.empregados, "Um empregado deve ser registrado na lista global de empregados")
        for i in range(3):
            self.empregado.vincular_empregado_hospital(i)
            self.assertEqual(len(self.empregado.hospitais), i+1)
        #relatorio_hospital_empregados = self.empregado.relatorio_hospital_empregados("E001")

    def testInsertEmpregado(self):
        self.assertNotEqual(self.empregado.nome, None)
        self.assertNotEqual(self.empregado.matricula, None)
        self.assertLessEqual(len(self.empregado.hospitais), 3, "Um Medico so pode estar vinculado a no maximo 3 hospitais")

    def testVinculoEmpregadoHospitalThrowsException(self):
        if (len(self.empregado.hospitais) == 3):
            self.assertRaises(RuntimeError, self.empregado.vincular_empregado_hospital, 4)

    #@unittest.skip("Aguardando desenvolvimento")
    def testVinculoEmpregadoHospitalExistente(self):
        if (2 in self.empregado.hospitais):
            self.assertRaises(RuntimeError, self.empregado.vincular_empregado_hospital, 2)
            #self.assertNotIn(2, self.medico.hospitais, "Nao se admite um empregado com mais de um vinculo em um mesmo hospital.")

    def testListaAtendimentos(self):
        self.assertListEqual(self.empregado.atendimentos, [], "Um empregado deve possuir uma lista de atendimentos")

    def testVinculoEmpregadoAtendimento(self):
        self.empregado.vincular_atendimento(2)
        self.assertEqual(len(self.empregado.atendimentos), 1)

class TesteMedico(unittest.TestCase):

    def setUp(self):
        self.medico = Medico.Medico("Dr. House","M001","Cardiologista")
        self.assertIn(self.medico, Medico.Medico.medicos, "Um medico deve ser registrado na lista global de medicos")
        self.assertIn(self.medico, Empregado.Empregado.empregados, "Um medico e um empregado e deve estar registrado na lista global de empregados")

    def testInsertMedico(self):
        self.assertNotEqual(self.medico.nome, None)
        self.assertNotEqual(self.medico.matricula, None)
        self.assertNotEqual(self.medico.especialidade, None)

class TesteEnfermeira(unittest.TestCase):

    def setUp(self):
        self.enfermeira = Enfermeira.Enfermeira("Maria dos Anjos","E001","Enfermeira chefe")
        self.assertIn(self.enfermeira, Enfermeira.Enfermeira.enfermeiras, "Uma enfermeira deve ser registrada na lista global de enfermeiras")
        self.assertIn(self.enfermeira, Empregado.Empregado.empregados, "Uma enfermeira e uma empregada e deve ser registrada na lista global de empregados")

    def testInsertEnfermeira(self):
        self.assertNotEqual(self.enfermeira.nome, None)
        self.assertNotEqual(self.enfermeira.matricula, None)
        self.assertNotEqual(self.enfermeira.cargo, None)

class TesteInternacao(unittest.TestCase):

    def setUp(self):
        self.hospital= Hospital.Hospital("Dr.Beda","H001","Rua do Gas")
        self.paciente = Paciente.Paciente("Paciente", "12345", 18)
        self.medico = Medico.Medico("Dr. House","M001","Cardiologista")        
        self.internacao = Internacao.Internacao("I001","05/02/2011", self.medico, self.paciente, self.hospital)
        self.empregado = Empregado.Empregado("Dr. House","M001")
        self.atendimento = Atendimento.Atendimento(self.empregado, self.internacao)

        self.internacao.vincular_medico(self.medico)
        self.assertIn(self.internacao, self.medico.internacoes)
        self.assertEqual(self.internacao.medico, self.medico)

        self.internacao.vincular_paciente(self.paciente)
        self.assertIn(self.internacao, self.paciente.internacoes)
        self.assertEqual(self.internacao.paciente, self.paciente)
        
        self.internacao.vincular_atendimento(self.atendimento)
        self.assertIn(self.atendimento, self.internacao.atendimentos)
        self.assertEqual(self.internacao.hospital, self.hospital)
        
        self.assertIn(self.internacao, self.hospital.internacoes)
        
        self.atendimento.vincular_empregado(self.empregado)
        self.assertEqual(self.atendimento.empregado, self.empregado)
        self.assertIn(self.atendimento, self.empregado.atendimentos)
        self.assertEqual(len(self.empregado.atendimentos), 1)
        
        self.assertIn(self.internacao, Internacao.Internacao.internacoes, "Uma internacao deve ser registrada na lista global de internacoes")

        relatorio_pacientes_internados_hospital_com_medicos_e_periodo = Internacao.Internacao.relatorio_pacientes_internados_hospital_com_medicos_e_periodo("H001")
        #self.assertIsInstance(relatorio_pacientes_internados_hospital_com_medicos_e_periodo, list)
        #Internacao.Internacao.relatorio_atendimentos_internacao = Internacao.relatorio_atendimentos_internacao("I001")
        #self.assertIsInstance(relatorio_atendimentos_internacao, list)
        
    def testInsertInternacao(self):
        self.assertNotEqual(self.internacao.codigo, None)
        self.assertNotEqual(self.internacao.data_inicio, None)
        self.assertNotEqual(self.internacao.medico, None)
        self.assertEqual(self.internacao.data_fim, None)
        self.assertNotEqual(self.internacao.paciente, None)
        self.assertNotEqual(self.internacao.hospital, None)

class TesteAtendimento(unittest.TestCase):

    def setUp(self):
        self.empregado = Empregado.Empregado("Dr. House","M001")
        self.hospital= Hospital.Hospital("Dr.Beda","H001","Rua do Gas")
        self.paciente = Paciente.Paciente("Paciente", "12345", 18)        
        self.internacao = Internacao.Internacao("I001","05/02/2011", "M001", self.paciente, self.hospital)
        self.atendimento = Atendimento.Atendimento(self.empregado, self.internacao)
        self.assertIn(self.atendimento, Atendimento.Atendimento.atendimentos, "Um atendimento deve ser registrado na lista global de atendimentos")

    def testPossuiEmpregado(self):
        self.assertNotEqual(self.atendimento.empregado, None)

    def testPossuiInternacao(self):
        self.assertNotEqual(self.atendimento.internacao, None)

if __name__== "__main__":
    unittest.main()

