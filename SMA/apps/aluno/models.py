from django.db import models

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    matricula = models.CharField(max_length=20, unique=True)
    periodo = models.CharField(max_length=20)
    uid = models.CharField(max_length=32, unique=True, null=True, blank=True)

    cursos = models.ManyToManyField("curso.Curso", through="aluno.AlunoCurso")
    disciplinas = models.ManyToManyField("disciplina.Disciplina", through="aluno.AlunoDisciplina")

    def __str__(self):
        return self.nome


class AlunoCurso(models.Model):
    aluno = models.ForeignKey("aluno.Aluno", on_delete=models.CASCADE)
    curso = models.ForeignKey("curso.Curso", on_delete=models.CASCADE)


class AlunoDisciplina(models.Model):
    aluno = models.ForeignKey("aluno.Aluno", on_delete=models.CASCADE)
    disciplina = models.ForeignKey("disciplina.Disciplina", on_delete=models.CASCADE)

