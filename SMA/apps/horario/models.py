from django.db import models

class Horarios(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField()
    hora = models.TimeField()

    disciplinas = models.ManyToManyField("disciplina.Disciplina", through="horario.DisciplinaHorario")

    def __str__(self):
        return f"{self.data} - {self.hora}"


class DisciplinaHorario(models.Model):
    disciplina = models.ForeignKey("disciplina.Disciplina", on_delete=models.CASCADE)
    horario = models.ForeignKey("horario.Horarios", on_delete=models.CASCADE)
