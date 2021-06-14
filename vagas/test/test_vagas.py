from django.test import TestCase
from vagas.models import *
from django.urls import reverse
from rest_framework import status
import json 


class VagasTestCase(TestCase):

    def setUp(self):

        self.data = {
                        "titulo": "Vaga Test",
                    }

        self.vaga = Vaga.objects.create(titulo='Vaga para teste')

        self.list_url = reverse('Vagas-list')


    def test_vaga_post(self):
        """ teste para verificar o post de vagas"""    
        response = self.client.post(self.list_url, self.data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


    def test_vaga_put(self):
        """ teste para verificar o put de vagas"""    
        data = {
            "titulo": "Programador Full Stack Sênior",
            "resumo": "Teste de resumo da vaga"
        }

        response = self.client.put('/vagas/'+str(self.vaga.id)+'/', data=data, content_type='application/json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def teste_vaga_get(self):
        """ teste para verificar o get de vagas"""
        
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def teste_vaga_delete(self):
        """ teste para verificar se é possivel deletar uma vaga"""
        
        response = self.client.delete('/vagas/1/')

        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
