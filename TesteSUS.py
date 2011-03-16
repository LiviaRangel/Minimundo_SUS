import unittest
import Hospital, Paciente, Medico, Enfermeira, Internacao, Atendimento, Empregado


class TesteHospital(unittest.TestCase):

    def setUp(self):
        self.hospital = Hospital.Hospital("Dr.Beda","H001","Rua do Gas")

    def testInsertHospital(self):
        self.assertNotEqual(self.hospital.nome, None)
        self.assertNotEqual(self.hospital.codigo, None)
        self.assertNotEqual(self.hospital.endereco, None)


    def testListaHospitais(self):
        self.assertListEqual(self.hospital.empregados, [], "Um hospital deve possuir uma lista de empregados")

    def testListaInternacoes(self):
        self.assertListEqual(self.hospital.internacoes, [], "Um hospital deve possuir uma lista de internacoes de pacientes")

    def testVinculoInternacoesHospital(self):
        self.hospital.vincular_internacao_hospital(1)
        self.assertEqual(len(self.hospital.internacoes), 1)

    def testVinculoEmpregadoHospital(self):
        self.hospital.vincular_empregado_hospital(1)
        self.assertEqual(len(self.hospital.empregados), 1)

class TestePaciente(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente.Paciente("Jose da Silva","P001","18")

    def testInsertPaciente(self):
        self.assertNotEqual(self.paciente.nome, None)
        self.assertNotEqual(self.paciente.codigo_seguro_social, None)
        self.assertNotEqual(self.paciente.idade, None)

    def testPossuiInternacoes(self):
        self.assertListEqual(self.paciente.internacoes, [], "Um paciente possui uma lista das internacoes que sofreu")


class TesteEmpregado(unittest.TestCase):
    def setUp(self):
        self.empregado = Empregado.Empregado("Dr. House","M001")
        for i in range(3):
            self.empregado.vincular_empregado_hospital(i)
            self.assertEqual(len(self.empregado.hospitais), i+1)


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
        self.empregado.vincular_empregado_atendimento(2)
        self.assertEqual(len(self.empregado.atendimentos), 1)

class TesteMedico(unittest.TestCase):

    def setUp(self):
        self.medico = Medico.Medico("Dr. House","M001","Cardiologista")

    def testInsertMedico(self):
        self.assertNotEqual(self.medico.nome, None)
        self.assertNotEqual(self.medico.matricula, None)
        self.assertNotEqual(self.medico.especialidade, None)

class TesteEnfermeira(unittest.TestCase):

    def setUp(self):
        self.enfermeira = Enfermeira.Enfermeira("Maria dos Anjos","E001","Enfermeira chefe")

    def testInsertEnfermeira(self):
        self.assertNotEqual(self.enfermeira.nome, None)
        self.assertNotEqual(self.enfermeira.matricula, None)
        self.assertNotEqual(self.enfermeira.cargo, None)

class TesteInternacao(unittest.TestCase):

    def setUp(self):
        self.internacao = Internacao.Internacao("I001","05/02/2011", "", "M001")

    def testInsertInternacao(self):
        self.assertNotEqual(self.internacao.codigo, None)
        self.assertNotEqual(self.internacao.data_inicio, None)
        self.assertNotEqual(self.internacao.medico, None)

    def testPossuiAtributoPaciente(self):
        self.assertEqual(self.internacao.paciente, None)

#class TesteMedicoExists(unittest.TestCase):

#class TestePacienteExists(unittest.TestCase):

class TesteAtendimento(unittest.TestCase):

    def setUp(self):
        self.atendimento = Atendimento.Atendimento()

    def testPossuiEmpregado(self):
        self.assertEqual(self.atendimento.empregado, None)

    def testPossuiInternacao(self):
        self.assertEqual(self.atendimento.internacao, None)

#class TesteInternacaoExists(unittest.TestCase):

#class TesteVincularMedico(unittest.TestCase):

#class TesteVincularEnfermeira(unittest.TestCase):

if __name__== "__main__":
    unittest.main()

