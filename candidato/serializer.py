from rest_framework import serializers
from candidato.models import Candidato


class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = ['id','nome','resumo','sexo','formacao','cep','email', 'avatar','data_cadastro']



