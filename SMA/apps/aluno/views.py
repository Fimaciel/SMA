from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

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
