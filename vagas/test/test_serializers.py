from django.db.models.query import InstanceCheckMeta
from django.test import TestCase
from vagas.models import *
from vagas.serializer import *
from candidato.models import Candidato

class VagaSerializerTestCase(TestCase):

    def setUp(self):
        self.vaga = Vaga(
            titulo='Vaga Teste'  
        )

        self.serializer = VagaSerializer(instance=self.vaga)


    def test_verifica_campos_serializados(self):
        """ teste  para verificar se os campos são serializados corretamente """

        data = self.serializer.data

        self.assertEquals(set(data.keys()),set(['titulo','resumo','descricao','tipo_contrato','remuneracao', 'beneficios']))
    
    def test_verifica_conteudo_campos_serializados(self):
        """ teste para veriricar se os campos estão sendo corretamente serializados """

        data = self.serializer.data

        self.assertEquals(data['titulo'], self.vaga.titulo)
        self.assertEquals(data['resumo'], self.vaga.resumo)
        self.assertEquals(data['descricao'], self.vaga.descricao)
        self.assertEquals(data['tipo_contrato'], self.vaga.tipo_contrato)
        self.assertEquals(data['remuneracao'], self.vaga.remuneracao)
        self.assertEquals(data['beneficios'], self.vaga.beneficios)


class CandidaturaSerializerTestCase(TestCase):

    def setUp(self):
        self.candidato = Candidato.objects.create(
            nome='Candidato Teste',
            email='email@teste.com.br'
        )

        self.vaga = Vaga.objects.create(
            titulo = 'vaga teste',
        )

        self.candidatura = Candidaturas(
            vaga=self.vaga,
            candidato=self.candidato
        )

        self.serializer = CandidaturasSerializer(instance=self.candidatura)


    def test_verifica_campos_serializados(self):
        """ teste  para verificar se os campos são serializados corretamente """

        data = self.serializer.data

        self.assertEquals(set(data.keys()),set(['id','candidato','vaga','status','data_cadastro']))

    def test_verifica_conteudo_campos_serializados(self):
        """ teste para veriricar se os campos estão sendo corretamente serializados """

        data = self.serializer.data 

        self.assertEquals(data['vaga'], self.candidatura.vaga.id)
        self.assertEquals(data['candidato'], self.candidatura.candidato.id)
        self.assertEquals(data['status'], self.candidatura.status)

class ListaCandidaturasSerializerTestCase(TestCase):

    def setUp(self):
        self.candidato = Candidato.objects.create(
            nome='Candidato Teste',
            email='email@teste.com.br'
        )

        self.vaga = Vaga.objects.create(
            titulo = 'vaga teste',
        )

        self.candidatura = Candidaturas.objects.create(
            vaga=self.vaga,
            candidato=self.candidato
        ) 

        self.serializer = ListaCandidaturasCandidatoSerializer(instance=self.candidatura)

    def test_verifica_campos_serializados(self):
        """ teste  para verificar se os campos são serializados corretamente """

        data = self.serializer.data

        self.assertEquals(set(data.keys()),set(['id_vaga','vaga_nome','status']))


    def test_verifica_conteudo_campos_serializados(self):
        """ teste para veriricar se os campos estão sendo corretamente serializados """

        data = self.serializer.data 

        self.assertEquals(data['id_vaga'], self.vaga.id)
        self.assertEquals(data['vaga_nome'], self.vaga.titulo)
        self.assertEquals(data['status'], self.candidatura.status)



class ListaCandidatoVagaSerializerTestCase(TestCase):

    def setUp(self):
        self.candidato = Candidato.objects.create(
            nome='Candidato Teste 22',
            email='email@teste.com.br'
        )

        self.vaga = Vaga.objects.create(
            titulo = 'vaga teste 22',
        )

        self.candidatura = Candidaturas.objects.create(
            vaga=self.vaga,
            candidato=self.candidato
        ) 

        self.serializer = ListaCandidatosVagaSerializer(instance=self.candidatura)

    def test_verifica_campos_serializados(self):
        """ teste  para verificar se os campos são serializados corretamente """

        data = self.serializer.data

        self.assertEquals(set(data.keys()),set(['id_candidato','candidato_nome','status']))


    def test_verifica_conteudo_campos_serializados(self):
        """ teste para veriricar se os campos estão sendo corretamente serializados """

        data = self.serializer.data 

        self.assertEquals(data['id_candidato'], self.candidato.id)
        self.assertEquals(data['candidato_nome'], self.candidato.nome)
        self.assertEquals(data['status'], self.candidatura.status)
