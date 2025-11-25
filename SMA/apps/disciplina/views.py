from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Disciplina
from .forms import DisciplinaForm

class DisciplinaListView(ListView):
    model = Disciplina
    template_name = 'disciplina/disciplina_list.html'
    context_object_name = 'disciplinas'
    paginate_by = 10

class DisciplinaCreateView(CreateView):
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'disciplina/disciplina_form.html'
    success_url = reverse_lazy('disciplina:disciplina_list')

class DisciplinaUpdateView(UpdateView):
    model = Disciplina
    form_class = DisciplinaForm
    template_name = 'disciplina/disciplina_form.html'
    success_url = reverse_lazy('disciplina:disciplina_list')

class DisciplinaDeleteView(DeleteView):
    model = Disciplina
    template_name = 'disciplina/disciplina_confirm_delete.html'
    success_url = reverse_lazy('disciplina:disciplina_list')