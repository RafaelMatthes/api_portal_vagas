from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from candidato.views import CandidatoViewSet
from vagas.views import VagasViewSet, CandidaturasViewSet, ListaCandidaturasCandidatoViewSet, ListaCandidatisVagaViewSet



router = routers.DefaultRouter()
router.register('candidatos', CandidatoViewSet, basename='Candidatos')
router.register('vagas', VagasViewSet, basename='Vagas')
router.register('candidaturas', CandidaturasViewSet, basename='Candidaturas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('candidatos/<int:pk>/candidaturas', ListaCandidaturasCandidatoViewSet.as_view()),
    path('vagas/<int:pk>/candidaturas', ListaCandidatisVagaViewSet.as_view()),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
