from django.db import models

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    quantidade_horas = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

