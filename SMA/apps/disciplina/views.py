from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Disciplina, Aula
from .forms import DisciplinaForm, AulaForm

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


class AulaListView(ListView):
    model = Aula
    template_name = "aula/aula_list.html"
    context_object_name = "aulas"


class AulaCreateView(CreateView):
    model = Aula
    form_class = AulaForm
    template_name = "aula/aula_form.html"
    success_url = reverse_lazy("disciplina:aula_list")


class AulaUpdateView(UpdateView):
    model = Aula
    form_class = AulaForm
    template_name = "aula/aula_form.html"
    success_url = reverse_lazy("disciplina:aula_list")


class AulaDeleteView(DeleteView):
    model = Aula
    template_name = "aula/aula_confirm_delete.html"
    success_url = reverse_lazy("disciplina:aula_list")
