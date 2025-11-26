from django.shortcuts import render, redirect, get_object_or_404
from .models import Horarios, DisciplinaHorario
from .forms import HorariosForm

def horarios_list(request):
    horarios = Horarios.objects.all()
    return render(request, 'horarios/list.html', {
        'horarios': horarios
    })

def horarios_create(request):
    if request.method == 'POST':
        form = HorariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('horarios_list')
    else:
        form = HorariosForm()

    return render(request, 'horarios/form.html', {
        'form': form,
        'titulo': 'Cadastrar Horário'
    })

def horarios_edit(request, horario_id):
    horario = get_object_or_404(Horarios, id=horario_id)

    if request.method == 'POST':
        form = HorariosForm(request.POST, instance=horario)
        if form.is_valid():
            form.save()
            return redirect('horarios_list')
    else:
        form = HorariosForm(instance=horario)

    return render(request, 'horarios/form.html', {
        'form': form,
        'titulo': 'Editar Horário'
    })


def horarios_delete(request, horario_id):
    horario = get_object_or_404(Horarios, id=horario_id)

    if request.method == 'POST':
        horario.delete()
        return redirect('horarios_list')

    return render(request, 'horarios/delete.html', {
        'horario': horario
    })
