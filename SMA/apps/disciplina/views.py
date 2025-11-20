from django.shortcuts import render, redirect, get_object_or_404
from .models import Disciplina
from .forms import DisciplinaForm

def disciplina_list(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'disciplina/list.html', {'disciplinas': disciplinas})

def disciplina_create(request):
    if request.method == 'POST':
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('disciplina_list')
    else:
        form = DisciplinaForm()

    return render(request, 'disciplina/form.html', {
        'form': form,
        'titulo': 'Cadastrar Disciplina'
    })

def disciplina_edit(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)

    if request.method == 'POST':
        form = DisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('disciplina_list')
    else:
        form = DisciplinaForm(instance=disciplina)

    return render(request, 'disciplina/form.html', {
        'form': form,
        'titulo': 'Editar Disciplina'
    })

def disciplina_delete(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, id=disciplina_id)

    if request.method == 'POST':
        disciplina.delete()
        return redirect('disciplina_list')

    return render(request, 'disciplina/delete.html', {'disciplina': disciplina})
