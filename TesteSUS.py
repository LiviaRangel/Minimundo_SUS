import unittest
import Hospital, Paciente, Medico, Enfermeira, Internacao, Atendimento


class TesteHospital(unittest.TestCase):

    def setUp(self):
        self.hospital = Hospital.Hospital("Dr.Beda","H001","Rua do Gas")

    def testInsertHospital(self):
        self.assertNotEqual(self.hospital.nome, None)
        self.assertNotEqual(self.hospital.codigo, None)
        self.assertNotEqual(self.hospital.endereco, None)


class TestePaciente(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente.Paciente("Jose da Silva","P001","18")

    def testInsertPaciente(self):
        self.assertNotEqual(self.paciente.nome, None)
        self.assertNotEqual(self.paciente.codigo_seguro_social, None)
        self.assertNotEqual(self.paciente.idade, None)


class TesteMedico(unittest.TestCase):

    def setUp(self):
        self.medico = Medico.Medico("Dr. House","M001","Cardiologista")
        for i in range(3):
            self.medico.hospitais.append(i)

    def testInsertMedico(self):
        self.assertNotEqual(self.medico.nome, None)
        self.assertNotEqual(self.medico.matricula, None)
        self.assertNotEqual(self.medico.especialidade, None)
        self.assertLessEqual(len(self.medico.hospitais), 3, "Um Medico so pode estar vinculado a no maximo 3 hospitais")

    @unittest.skip("Aguardando desenvolvimento")
    def testVinculoMedicoHospitalThrowsException(self):
        if (len(self.medico.hospitais) == 3):
            self.assertRaises(RuntimeError, self.medico.vincular_medico_hospital, 4)

    @unittest.skip("Aguardando desenvolvimento")
    def testVinculoMedicoHospitalExistente(self):
        if (2 in self.medico.hospitais):
            self.assertRaises(AttributeError, self.medico.vincular_medico_hospital, 2)
            #self.assertNotIn(2, self.medico.hospitais, "Nao se admite um empregado com mais de um vinculo em um mesmo hospital.")

class TesteEnfermeira(unittest.TestCase):

    def setUp(self):
        self.enfermeira = Enfermeira.Enfermeira("Maria dos Anjos","E001","Enfermeira chefe")
        for i in range(3):
            self.enfermeira.hospitais.append(i)

    def testInsertEnfermeira(self):
        self.assertNotEqual(self.enfermeira.nome, None)
        self.assertNotEqual(self.enfermeira.matricula, None)
        self.assertNotEqual(self.enfermeira.cargo, None)

    @unittest.skip("Aguardando desenvolvimento")
    def testVinculoEnfermeiraHospitalThrowsException(self):
        if (len(self.enfermeira.hospitais) == 3):
            self.assertRaises(RuntimeError, self.enfermeira.vincular_enfermeira_hospital, 4)

    @unittest.skip("Aguardando desenvolvimento")
    def testVinculoEnfermeiraHospitalExistente(self):
        if (2 in self.enfermeira.hospitais):
            self.assertRaises(AttributeError, self.enfermeira.vincular_enfermeira_hospital, 2)
            #self.assertNotIn(2, self.enfermeira.hospitais, "Nao se admite um empregado com mais de um vinculo em um mesmo hospital.")


class TesteInternacao(unittest.TestCase):

    def setUp(self):
        self.internacao = Internacao.Internacao("I001","05/02/2011", "", "M001","P001")

    def testInsertInternacao(self):
        self.assertNotEqual(self.internacao.codigo, None)
        self.assertNotEqual(self.internacao.data_inicio, None)
        self.assertNotEqual(self.internacao.medico, None)
        self.assertNotEqual(self.internacao.paciente, None)

#class TesteMedicoExists(unittest.TestCase):

#class TestePacienteExists(unittest.TestCase):

class TesteAtendimento(unittest.TestCase):

    def setUp(self):
        self.atendimento = Atendimento.Atendimento("I001","M001")

    def testInsertAtendimento(self):
        self.assertNotEqual(self.atendimento.internacao, None)
        self.assertNotEqual(self.atendimento.responsavel, None)

#class TesteInternacaoExists(unittest.TestCase):

#class TesteVincularMedico(unittest.TestCase):

#class TesteVincularEnfermeira(unittest.TestCase):

if __name__== "__main__":
    unittest.main()

