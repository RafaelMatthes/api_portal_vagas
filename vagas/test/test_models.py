from django.test import TestCase
from candidato.models import Candidato
from vagas.models import Vaga, Candidaturas
from django.urls import reverse
from rest_framework import status


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


class CandidaturaTest(TestCase):

    def setUp(self):
        self.candidato = Candidato.objects.create(
            nome='Candidato Teste',
            email='email@teste.com.br'
        )

        self.vaga = Vaga.objects.create(
            titulo = 'vaga teste',
        )

        self.list_url = reverse('Candidaturas-list')

    def test_candidatura_get(self):
        """ verifica GET candidaturas """

        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_candidatura_post(self):
        """ teste para verificar o post de candidaturas """

        itens = {
                    "status": '',
                    "data_cadastro": '',
                    "candidato": self.candidato.id,
                    "vaga":  self.vaga.id
                }

        response = self.client.post(self.list_url, itens)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    