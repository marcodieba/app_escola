from rest_framework import viewsets
from .models import Atividade
from .serializers import AtividadeSerializer

class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer