from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from candidato.models import Candidato
from candidato.serializer import CandidatoSerializer


class CandidatoViewSet(viewsets.ModelViewSet):
    """ Exibe todos os Candidatos """

    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
    http_method_names = ['get','post', 'put', 'path']
    
    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(CandidatoViewSet, self).dispatch(*args, **kwargs)


