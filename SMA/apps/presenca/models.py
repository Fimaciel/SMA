from django.db import models
from apps.aluno.models import Aluno

class Presencas(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    horario_entrada = models.TimeField()
    horario_saida = models.TimeField()

    alunos = models.ManyToManyField(Aluno, through="PresencaAluno")

    def __str__(self):
        return f"Presença {self.id} - {self.data}"
    

class PresencaAluno(models.Model):
    presenca = models.ForeignKey(Presencas, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
