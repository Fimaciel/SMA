from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso
from .forms import CursoForm

# LISTAR
def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/list.html', {'cursos': cursos})

# CRIAR
def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm()

    return render(request, 'curso/form.html', {'form': form, 'titulo': 'Cadastrar Curso'})

# EDITAR
def curso_edit(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm(instance=curso)

    return render(request, 'curso/form.html', {'form': form, 'titulo': 'Editar Curso'})

# DELETAR
def curso_delete(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        curso.delete()
        return redirect('curso_list')

    return render(request, 'curso/delete.html', {'curso': curso})
