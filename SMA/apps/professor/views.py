from django.shortcuts import render, redirect, get_object_or_404
from .models import Professor, ProfessorDisciplina
from .forms import ProfessorForm, ProfessorDisciplinaForm

def professor_list(request):
    professores = Professor.objects.all()
    return render(request, 'professor/list.html', {
        'professores': professores
    })

def professor_create(request):
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm()

    return render(request, 'professor/form.html', {
        'form': form,
        'titulo': 'Cadastrar Professor'
    })

def professor_edit(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)

    if request.method == 'POST':
        form = ProfessorForm(request.POST, instance=professor)
        if form.is_valid():
            form.save()
            return redirect('professor_list')
    else:
        form = ProfessorForm(instance=professor)

    return render(request, 'professor/form.html', {
        'form': form,
        'titulo': 'Editar Professor'
    })

def professor_delete(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)

    if request.method == 'POST':
        professor.delete()
        return redirect('professor_list')

    return render(request, 'professor/delete.html', {
        'professor': professor
    })
