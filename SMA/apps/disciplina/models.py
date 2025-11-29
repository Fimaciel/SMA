from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    alunos = models.ManyToManyField("aluno.Aluno", related_name="disciplinas_relacionadas")


    def __str__(self):
        return self.nome


class Aula(models.Model):
    disciplina = models.ForeignKey("disciplina.Disciplina", on_delete=models.CASCADE)

    professor = models.ForeignKey(
        "professor.Professor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    curso = models.ForeignKey(
        "curso.Curso",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    data = models.DateField()
    horario_inicio = models.TimeField(null=True, blank=True)
    horario_fim = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.disciplina.nome} - {self.data}"