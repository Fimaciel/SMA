from django.db import models

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    disciplinas = models.ManyToManyField(
        "disciplina.Disciplina",
        through="curso.CursoDisciplina"
    )

    def __str__(self):
        return self.nome


class CursoDisciplina(models.Model):
    curso = models.ForeignKey("curso.Curso", on_delete=models.CASCADE)
    disciplina = models.ForeignKey("disciplina.Disciplina", on_delete=models.CASCADE)
