from django.test import TestCase
from candidato.models import Candidato
from candidato.serializer import CandidatoSerializer


class CandidatoTestSerializerTestCase(TestCase):
    
    def setUp(self):
        self.candidato = Candidato(
            nome='Candidato Teste',
            resumo='resumo do candidato',
            sexo='M',
            formacao='EB',
            cep='89069055',
            email='email@teste.com.br'
        )

        self.serializer = CandidatoSerializer(instance=self.candidato)

    def test_verifica_campos_serializados(self):
        """ teste para verificar os campos serializados """
    
        data = self.serializer.data

        self.assertEquals(set(data.keys()), set(['id','nome','resumo','sexo', 'formacao','cep','email','avatar','data_cadastro']))


    def test_verifica_conteudo_campos_serializados(self):
        """teste que verifica o conteúdo dos campos serializados """

        data = self.serializer.data

        self.assertEquals(data['id'], self.candidato.id)
        self.assertEquals(data['nome'], self.candidato.nome)
        self.assertEquals(data['resumo'], self.candidato.resumo)
        self.assertEquals(data['sexo'], self.candidato.sexo)
        self.assertEquals(data['formacao'], self.candidato.formacao)
        self.assertEquals(data['cep'], self.candidato.cep)
        self.assertEquals(data['email'], self.candidato.email)


