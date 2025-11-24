from django.shortcuts import render, redirect, get_object_or_404
from .models import Presencas, PresencaAluno
from .forms import PresencasForm, PresencaAlunoForm

def presencas_list(request):
    presencas = Presencas.objects.all()
    return render(request, 'presencas/list.html', {
        'presencas': presencas
    })

def presencas_create(request):
    if request.method == 'POST':
        form = PresencasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('presencas_list')
    else:
        form = PresencasForm()

    return render(request, 'presencas/form.html', {
        'form': form,
        'titulo': 'Cadastrar Presença'
    })


def presencas_edit(request, presenca_id):
    presenca = get_object_or_404(Presencas, id=presenca_id)

    if request.method == 'POST':
        form = PresencasForm(request.POST, instance=presenca)
        if form.is_valid():
            form.save()
            return redirect('presencas_list')
    else:
        form = PresencasForm(instance=presenca)

    return render(request, 'presencas/form.html', {
        'form': form,
        'titulo': 'Editar Presença'
    })

def presencas_delete(request, presenca_id):
    presenca = get_object_or_404(Presencas, id=presenca_id)

    if request.method == 'POST':
        presenca.delete()
        return redirect('presencas_list')

    return render(request, 'presencas/delete.html', {
        'presenca': presenca
    })
