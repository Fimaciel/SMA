from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoForm
from .models import Aluno

# CREATE - Página de formulário
def create(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alunos_index') 
    else:
        form = AlunoForm()
    return render(request, 'aluno/create.html', {'form': form})


# READ - Listar todos os alunos
def index(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/index.html', {'alunos': alunos})


# UPDATE - Editar um aluno existente
def edit(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save() 
        return redirect('alunos_index')
    return render(request, 'aluno/edit.html', {'form': form, 'aluno': aluno})


# DELETE - Excluir um aluno
def destroy(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('alunos_index')
    return render(request, 'aluno/confirm_delete.html', {'aluno': aluno})
