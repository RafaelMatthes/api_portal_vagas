from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from candidato.views import CandidatoViewSet



router = routers.DefaultRouter()
router.register('candidatos', CandidatoViewSet, basename='Candidatos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
