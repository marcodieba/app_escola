from django.urls import path
from .views import ranking
from .views import dashboard

from rest_framework.routers import DefaultRouter
from .views import PontuacaoViewSet

router = DefaultRouter()
router.register('pontuacoes', PontuacaoViewSet)

urlpatterns = router.urls


urlpatterns += [
    path('ranking/', ranking),
    path('dashboard/', dashboard),
]