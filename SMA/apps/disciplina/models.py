from django.db import models

class Disciplina(models.Model):
    id = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=100) 
    carga_horaria = models.PositiveIntegerField() 

    def __str__(self): return self.nome