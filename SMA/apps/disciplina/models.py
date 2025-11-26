from django.db import models

class Disciplina(models.Model):
    id = models.AutoField(primary_key=True) 
    nome = models.CharField(max_length=100) 
    carga_horaria = models.PositiveIntegerField() 

    def __str__(self): return self.nome


class Aula(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data = models.DateField()
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()

    def __str__(self):
        return f"{self.disciplina.nome} - {self.data}"
