from rest_framework.routers import DefaultRouter
from .views import AtividadeViewSet

router = DefaultRouter()
router.register('atividades', AtividadeViewSet)

urlpatterns = router.urls