from rest_framework import serializers
from candidato.models import Candidato


class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        exclude = ['data_cadastro']



