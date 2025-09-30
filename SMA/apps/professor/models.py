from django.db import models
from apps.disciplina.models import Disciplina

class Professor(models.Model): 
    id = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=100) 
    cpf = models.CharField(max_length=14, unique=True) 
    data_nascimento = models.DateField() 
    materia = models.CharField(max_length=100)


    def __str__(self): return self.nome

class ProfessorDisciplina(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

