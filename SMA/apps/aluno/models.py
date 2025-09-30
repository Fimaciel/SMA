from django.db import models
from apps.disciplina.models import Disciplina
from apps.curso.models import Curso

class Aluno(models.Model): 
    id = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=100) 
    cpf = models.CharField(max_length=14, unique=True) 
    data_nascimento = models.DateField() 
    matricula = models.CharField(max_length=20, unique=True) 
    periodo = models.CharField(max_length=20) 
    uid = models.CharField(max_length=32, unique=True)  # UID em HEX (ex.: "DEADBEEF")

    
    cursos = models.ManyToManyField(Curso, through="AlunoCurso") 
    disciplinas = models.ManyToManyField(Disciplina, through="AlunoDisciplina") 
    

    def __str__(self): return self.nome
    
    
class AlunoCurso(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    

class AlunoDisciplina(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
