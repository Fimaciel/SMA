from django import forms
from .models import Professor, ProfessorDisciplina

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'cpf', 'data_nascimento', 'materia']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'})
        }


class ProfessorDisciplinaForm(forms.ModelForm):
    class Meta:
        model = ProfessorDisciplina
        fields = ['professor', 'disciplina']
