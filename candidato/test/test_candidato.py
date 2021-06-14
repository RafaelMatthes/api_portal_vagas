from django.test import TestCase
from candidato.models import *
from django.urls import reverse
from rest_framework import status
import json 


class candidatosTestCase(TestCase):

    def setUp(self):

        self.data = {
                "nome": "Teste",
                "resumo": " resumo teste",
                "sexo": "M",
                "formacao": "EM",
                "cep": "89069055",
                "email": "teste@mail.com"
            }

        self.candidato = Candidato.objects.create(nome='candidato para teste')

        self.list_url = reverse('Candidatos-list')


    def test_candidato_post(self):
        """ teste para verificar o post de candidatos"""    
        response = self.client.post(self.list_url, self.data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


    def test_candidato_put(self):
        """ teste para verificar o put de candidatos"""    
        data = json.dumps({
                   "nome": "Teste 223",
                    "resumo": "resumo teste",
                    "sexo": "M",
                    "formacao": "EM",
                    "cep": "89069055",
                    "email": "teste@mail.com"
            })

        response = self.client.put(self.list_url+str(self.candidato.id)+'/', data=data,  content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def teste_candidato_get(self):
        """ teste para verificar o get de candidatos"""
        
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def teste_candidato_delete(self):
        """ teste para verificar se é possivel deletar uma candidato"""
        
        response = self.client.delete('/candidatos/1/')

        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
