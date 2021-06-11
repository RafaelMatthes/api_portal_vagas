from django.test import TestCase
from candidato.models import Candidato

class CandidatoModelTestCase(TestCase):

    def setUp(self):
        self.candidato = Candidato(
            nome='Candidato Teste',
            email='email@teste.com.br'
        )


    def test_verifica_atributos_candidato(self):
        """ este teste deverá verificar a criação de cadidatos """

        self.assertEquals(self.candidato.nome, 'Candidato Teste')
        self.assertEquals(self.candidato.resumo, '')
        self.assertEquals(self.candidato.sexo, 'N')
        self.assertEquals(self.candidato.formacao, 'ND')
        self.assertEquals(self.candidato.cep, '' )
        self.assertEquals(self.candidato.email, 'email@teste.com.br')
        self.assertEquals(self.candidato.avatar, '')
        