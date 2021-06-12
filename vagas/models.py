from django.db import models
from django.utils import timezone
from candidato.models import Candidato

TIPOS_CHOICE = [
    ('0', 'a combinar'),
    ('1', 'CLT'),
    ('2', 'PJ'),
    ('3', 'Temporário')
]

class Vaga(models.Model):
    titulo  = models.CharField(max_length=60)
    resumo = models.CharField(max_length=125, default='')
    descricao = models.CharField(max_length=255, default='')
    tipo_contrato = models.CharField(max_length=2, choices=TIPOS_CHOICE, default='1')
    remuneracao = models.CharField(max_length=15, default='a combinar')
    beneficios = models.CharField(max_length=255, blank=True, default='')
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo


STATUS_CHOICE = [
    ('AC','Aguardando contato'),
    ('AG','Entrevista agendada'),
    ('AF','Aguardando feedback'),
    ('PE','Processo encerrado'),
]

class Candidaturas(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICE, default='AC')
    data_cadastro = models.DateTimeField(default=timezone.now)




