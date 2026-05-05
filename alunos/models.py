from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    turma = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome