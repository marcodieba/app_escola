from rest_framework.decorators import action
from django.db.models import Sum
from rest_framework.decorators import api_view

from alunos.models import Aluno
from rest_framework import viewsets
from .models import Pontuacao
from .serializers import PontuacaoSerializer

class PontuacaoViewSet(viewsets.ModelViewSet):
    queryset = Pontuacao.objects.all()
    serializer_class = PontuacaoSerializer

    @action(detail=False, methods=['post'])
    def sync(self, request):
        dados = request.data.get("pontuacoes", [])

        criados = 0

        for item in dados:
            if not Pontuacao.objects.filter(local_id=item["local_id"]).exists():
                Pontuacao.objects.create(
                    local_id=item["local_id"],
                    aluno_id=item["aluno_id"],
                    atividade_id=item["atividade_id"],
                    pontos_ganhos=item["pontos_ganhos"]
                )
                criados += 1

        return Response({
            "status": "ok",
            "novos_registros": criados
        })



@api_view(['GET'])
def dashboard(request):
    total_alunos = Aluno.objects.count()
    total_pontos = Pontuacao.objects.aggregate(
        total=Sum('pontos_ganhos')
    )["total"] or 0

    return Response({
        "total_alunos": total_alunos,
        "total_pontos": total_pontos
    })


@api_view(['GET'])
def ranking(request):
    data = (
        Pontuacao.objects
        .values('aluno__id', 'aluno__nome')
        .annotate(total=Sum('pontos_ganhos'))
        .order_by('-total')
    )

    return Response(data)