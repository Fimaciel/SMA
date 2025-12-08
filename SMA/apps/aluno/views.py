from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from .forms import AlunoForm
from .models import Aluno


class AlunoListView(ListView):
    model = Aluno
    template_name = 'aluno/aluno_list.html'
    context_object_name = 'alunos'
    paginate_by = 10


class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno/aluno_form.html'
    success_url = reverse_lazy('aluno:aluno_list')


class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno/aluno_form.html'
    success_url = reverse_lazy('aluno:aluno_list')


class AlunoDeleteView(DeleteView):
    model = Aluno
    template_name = 'aluno/aluno_confirm_delete.html'
    success_url = reverse_lazy('aluno:aluno_list')


@require_POST
def toggle_rfid(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    
    if aluno.uid:
        aluno.uid = None
        status = 'desativado'
        message = 'RFID desativado. Adicione manualmente no cadastro do aluno.'
    else:
        status = 'pendente'
        message = 'Para ativar o RFID, edite o aluno e adicione o UID manualmente.'
    
    aluno.save()
    
    return JsonResponse({
        'success': True,
        'status': status,
        'uid': aluno.uid,
        'message': message
    })
