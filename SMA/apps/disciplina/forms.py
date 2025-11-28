from django import forms
from .models import Aula
from apps.disciplina.models import Disciplina
from apps.professor.models import Professor
from apps.curso.models import Curso
from apps.horario.models import Horarios
from apps.aluno.models import Aluno


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ["nome", "descricao", "alunos"]
        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control'}),
            "descricao": forms.Textarea(attrs={'class': 'form-control'}),
            "alunos": forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

        
class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = [
            "disciplina",
            "professor",
            "curso",
            "horario",
            "data",
            "horario_inicio",
            "horario_fim",
            "alunos",
        ]
        widgets = {
            "data": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "horario_inicio": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "horario_fim": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "alunos": forms.CheckboxSelectMultiple(),
        }
