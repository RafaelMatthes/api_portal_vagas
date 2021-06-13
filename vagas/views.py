from rest_framework import viewsets, generics
from vagas.models import Vaga, Candidaturas
from vagas.serializer import VagaSerializer, CandidaturasSerializer, ListaCandidaturasCandidatoSerializer, ListaCandidatosVagaSerializer


class VagasViewSet(viewsets.ModelViewSet):
    """ viewset para exibir Vagas """ 

    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
    http_method_names = ['get','post', 'put', 'path']


class CandidaturasViewSet(viewsets.ModelViewSet):
    """ viewset para exibir candidaturas """

    queryset = Candidaturas.objects.all()
    serializer_class = CandidaturasSerializer
    http_method_names = ['get','post', 'put', 'path']

class ListaCandidaturasCandidatoViewSet(generics.ListAPIView):
    """ listand as candidaturas de um candidato """

    def get_queryset(self):
        queryset = Candidaturas.objects.filter(candidato=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaCandidaturasCandidatoSerializer

class ListaCandidatisVagaViewSet(generics.ListAPIView):
    """ listand as candidaturas de um candidato """

    def get_queryset(self):
        queryset = Candidaturas.objects.filter(vaga=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaCandidatosVagaSerializer