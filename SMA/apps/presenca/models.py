from django.db import models
from apps.aluno.models import Aluno
from apps.disciplina.models import Aula

class PresencaAluno(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, null=True, blank=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    
    horario_entrada = models.DateTimeField(null=True, blank=True)
    horario_saida = models.DateTimeField(null=True, blank=True)

    tempo_total = models.IntegerField(default=0)  # minutos
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.aluno.nome} - {self.aula}"


class RegistroRFID(models.Model):
    presenca = models.ForeignKey(PresencaAluno, on_delete=models.CASCADE)
    horario = models.DateTimeField()
    tipo = models.CharField(max_length=10, choices=(("IN","Entrada"), ("OUT","Saída")))
