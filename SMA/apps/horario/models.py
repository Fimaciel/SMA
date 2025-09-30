from django.db import models
from apps.disciplina.models import Disciplina

class Horarios(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    hora = models.TimeField()

    disciplinas = models.ManyToManyField(Disciplina, through="DisciplinaHorario")

    def __str__(self):
        return f"{self.data} - {self.hora}"

class DisciplinaHorario(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horarios, on_delete=models.CASCADE)
