from django.db import models
from django.utils import timezone


GENERO_CHOICE = [
    ('N','Não Informado'),
    ('M','Masculino'),
    ('F','Feminino')
]

FORMACAO_CHOICE = [
    ('ND','Não Informado'),
    ('EB','Ensino Básico'),
    ('EM','Ensino Médio'),
    ('ES','Ensino Superior'),
]

class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    resumo = models.CharField(max_length=255, default='')
    sexo = models.CharField(max_length=1, choices=GENERO_CHOICE, default='N')
    formacao = models.CharField(max_length=2, choices=FORMACAO_CHOICE, default='ND')
    cep = models.CharField(max_length=8, default='')
    email = models.CharField(max_length=100)
    avatar = models.ImageField(blank=True)
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome



