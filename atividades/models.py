from django.db import models

class Atividade(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    pontos = models.IntegerField()
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo