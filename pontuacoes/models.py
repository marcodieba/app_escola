from django.db import models
from alunos.models import Aluno
from atividades.models import Atividade

class Pontuacao(models.Model):
    local_id = models.CharField(max_length=100, unique=True)

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)

    pontos_ganhos = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno} - {self.pontos_ganhos}"