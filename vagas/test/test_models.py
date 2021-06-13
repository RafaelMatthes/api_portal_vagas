from django.test import TestCase
from candidato.models import Candidato
from vagas.models import Vaga, Candidaturas


class VagaModelTest(TestCase):

    def setUp(self):
        self.vaga = Vaga(
            titulo = 'vaga teste',
        )

    def test_verifica_atributos_modelo(self):
        """ teste para verificar atributos default """

        self.assertEquals(self.vaga.titulo, 'vaga teste')
        self.assertEquals(self.vaga.resumo, '')
        self.assertEquals(self.vaga.descricao, '')
        self.assertEquals(self.vaga.tipo_contrato, '1')
        self.assertEquals(self.vaga.remuneracao, 'a combinar')
        self.assertEquals(self.vaga.beneficios, '')

class CandidaturasModelTest(TestCase):

    def setUp(self):
        self.candidato = Candidato.objects.create(
            nome='Candidato Teste',
            email='email@teste.com.br'
        )

        self.vaga = Vaga.objects.create(
            titulo = 'vaga teste',
        )

        self.candidatura = Candidaturas(vaga=self.vaga,candidato=self.candidato)

    def test_verifica_atributos_modelo(self):
        """ teste para verificar atributos default """

        self.assertEquals(self.candidatura.candidato.id,  self.candidato.id)
        self.assertEquals(self.candidatura.vaga.id,  self.vaga.id)
        self.assertEquals(self.candidatura.status,  'AC')
