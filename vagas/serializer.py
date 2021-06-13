from rest_framework import serializers
from vagas.models import Vaga, Candidaturas


class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = ['titulo', 'resumo', 'descricao', 'tipo_contrato', 'remuneracao', 'beneficios']
        

class CandidaturasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidaturas
        fields = '__all__'

class ListaCandidaturasCandidatoSerializer(serializers.ModelSerializer):
    """ deverá  exibir as candidaturas realizadas pelo candidato """
    vaga_nome = serializers.ReadOnlyField(source='vaga.titulo')
    id_vaga = serializers.ReadOnlyField(source='vaga.id')
    class Meta:
        model = Candidaturas
        fields = ['id_vaga','vaga_nome','status'] 


class ListaCandidatosVagaSerializer(serializers.ModelSerializer):
    """ deverá listar os candidatos que realizaram a candidatura para a vaga solicitada """
    candidato_nome = serializers.ReadOnlyField(source='candidato.nome')
    id_candidato = serializers.ReadOnlyField(source='candidato.id')
    
    class Meta:
        model = Candidaturas
        fields = ['id_candidato','candidato_nome','status']