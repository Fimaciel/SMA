from django import forms
from .models import Presencas, PresencaAluno

class PresencasForm(forms.ModelForm):
    class Meta:
        model = Presencas
        fields = ['data', 'horario_entrada', 'horario_saida', 'alunos']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario_entrada': forms.TimeInput(attrs={'type': 'time'}),
            'horario_saida': forms.TimeInput(attrs={'type': 'time'}),
            'alunos': forms.CheckboxSelectMultiple(),
        }
