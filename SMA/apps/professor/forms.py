from django import forms
from .models import Professor, Disciplina

class ProfessorForm(forms.ModelForm):
    disciplinas = forms.ModelMultipleChoiceField(
        queryset=Disciplina.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False, # Making it optional
        label="Disciplinas lecionadas"
    )

    class Meta:
        model = Professor
        fields = ['nome', 'cpf', 'data_nascimento', 'materia', 'disciplinas']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'materia': forms.TextInput(attrs={'class': 'form-control'}),
        }
