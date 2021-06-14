from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from candidato.views import CandidatoViewSet
from vagas.views import VagasViewSet, CandidaturasViewSet, ListaCandidaturasCandidatoViewSet, ListaCandidatisVagaViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Portal de Vagas - API",
      default_version='v1',
      description="Api desenvolvida para demonstração.",
      terms_of_service="https://www.linkedin.com/in/rafael-matthes-59712342/",
      contact=openapi.Contact(email="rafael.matthes@live.com"),
      license=openapi.License(name="#"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()
router.register('candidatos', CandidatoViewSet, basename='Candidatos')
router.register('vagas', VagasViewSet, basename='Vagas')
router.register('candidaturas', CandidaturasViewSet, basename='Candidaturas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('candidatos/<int:pk>/candidaturas', ListaCandidaturasCandidatoViewSet.as_view()),
    path('vagas/<int:pk>/candidaturas', ListaCandidatisVagaViewSet.as_view()),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
