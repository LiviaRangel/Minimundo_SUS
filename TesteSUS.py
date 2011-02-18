import unittest
import Hospital, Paciente, Medico, Enfermeira, Internacao, Atendimento


class TesteHospital(unittest.TestCase):

    def setUp(self):
        self.hospital = Hospital.Hospital("Dr.Beda","H001","Rua do Gas")

    def testInsertHospital(self):
        assert self.hospital.nome != None
        assert self.hospital.codigo != None
        assert self.hospital.endereco != None


class TestePaciente(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente.Paciente("Jose da Silva","P001","18")

    def testInsertPaciente(self):
        assert self.paciente.nome != None
        assert self.paciente.seguro != None
        assert self.paciente.idade != None


class TesteMedico(unittest.TestCase):

    def setUp(self):
        self.medico = Medico.Medico("Dr. House","M001","Cardiologista")

    def testInsertMedico(self):
        assert self.medico.nome != None
        assert self.medico.matricula != None
        assert self.medico.especialidade != None


class TesteEnfermeira(unittest.TestCase):

    def setUp(self):
        self.enfermeira = Enfermeira.Enfermeira("Maria dos Anjos","E001","Enfermeira chefe")

    def testInsertEnfermeira(self):
        assert self.enfermeira.nome != None
        assert self.enfermeira.matricula != None
        assert self.enfermeira.cargo != None


class TesteInternacao(unittest.TestCase):

    def setUp(self):
        self.internacao = Internacao.Internacao("I001","05/02/2011", "", "M001","P001")

    def testInsertInternacao(self):
        assert self.internacao.codigo != None
        assert self.internacao.data_inicio != None
        assert self.internacao.medico != None
        assert self.internacao.paciente != None

#class TesteMedicoExists(unittest.TestCase):

#class TestePacienteExists(unittest.TestCase):

class TesteAtendimento(unittest.TestCase):

    def setUp(self):
        self.atendimento = Atendimento.Atendimento("I001","M001")

    def testInsertAtendimento(self):
        assert self.atendimento.internacao != None
        assert self.atendimento.responsavel != None

#class TesteInternacaoExists(unittest.TestCase):

#class TesteVincularMedico(unittest.TestCase):

#class TesteVincularEnfermeira(unittest.TestCase):

if __name__== "__main__":
    unittest.main()
