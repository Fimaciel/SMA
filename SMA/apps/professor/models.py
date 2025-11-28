from django.db import models

class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    materia = models.CharField(max_length=100, null=True, blank=True)

    cursos = models.ManyToManyField("curso.Curso", blank=True)

    def __str__(self):
        return self.nome


class ProfessorDisciplina(models.Model):
    professor = models.ForeignKey("professor.Professor", on_delete=models.CASCADE)
    disciplina = models.ForeignKey("disciplina.Disciplina", on_delete=models.CASCADE)
