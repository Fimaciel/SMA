from django.db import models

class PresencaAluno(models.Model):
    aula = models.ForeignKey("disciplina.Aula", on_delete=models.CASCADE, null=True, blank=True)
    aluno = models.ForeignKey("aluno.Aluno", on_delete=models.CASCADE)

    horario_entrada = models.DateTimeField(null=True, blank=True)
    horario_saida = models.DateTimeField(null=True, blank=True)

    tempo_total = models.IntegerField(default=0)
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.aluno.nome} - {self.aula}"


class RegistroRFID(models.Model):
    uid = models.CharField(max_length=32, null=True, blank=True)

    presenca = models.ForeignKey("presenca.PresencaAluno", on_delete=models.CASCADE, null=True, blank=True)

    horario = models.DateTimeField()
    tipo = models.CharField(
        max_length=10,
        choices=(("IN", "Entrada"), ("OUT", "Saída"))
    )

    def __str__(self):
        return f"{self.uid} - {self.tipo} - {self.horario}"
