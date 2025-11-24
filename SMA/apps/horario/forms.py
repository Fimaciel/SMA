from django import forms
from .models import Horarios, DisciplinaHorario

class HorariosForm(forms.ModelForm):
    class Meta:
        model = Horarios
        fields = ['data', 'hora', 'disciplinas']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'disciplinas': forms.CheckboxSelectMultiple()
        }
