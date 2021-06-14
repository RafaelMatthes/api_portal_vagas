from rest_framework import viewsets, generics
from vagas.models import Vaga, Candidaturas
from vagas.serializer import VagaSerializer, CandidaturasSerializer, ListaCandidaturasCandidatoSerializer, ListaCandidatosVagaSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class VagasViewSet(viewsets.ModelViewSet):
    """ viewset para exibir Vagas """ 

    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
    http_method_names = ['get','post', 'put', 'path']

    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(VagasViewSet, self).dispatch(*args, **kwargs)


class CandidaturasViewSet(viewsets.ModelViewSet):
    """ viewset para exibir candidaturas """

    queryset = Candidaturas.objects.all()
    serializer_class = CandidaturasSerializer
    http_method_names = ['get','post', 'put', 'path']

    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(CandidaturasViewSet, self).dispatch(*args, **kwargs)

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
