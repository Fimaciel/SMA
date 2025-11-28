from django import forms
from .models import Professor
from apps.disciplina.models import Disciplina

class ProfessorForm(forms.ModelForm):
    disciplinas = forms.ModelMultipleChoiceField(
        queryset=Disciplina.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check'}),
        required=False,
        label="Disciplinas lecionadas"
    )

    class Meta:
        model = Professor
        fields = ['nome', 'cpf', 'data_nascimento', 'disciplinas']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
