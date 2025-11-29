from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Disciplina, Aula
from .forms import DisciplinaForm, AulaForm
from django.http import JsonResponse
from apps.presenca.models import RegistroRFID as Presenca
from django.utils.timezone import make_aware, datetime


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

class AulaView(DetailView):
    model = Aula
    template_name = "aula/aula_view.html"
    context_object_name = "aula"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        disciplina = self.object.disciplina
        context["alunos"] = disciplina.alunos.all()


        return context


def presencas_json(request, pk):
    aula = Aula.objects.get(pk=pk)
    disciplina = aula.disciplina
    alunos = disciplina.alunos.all()

    # período da aula
    inicio = make_aware(datetime.combine(aula.data, aula.horario_inicio))
    fim = make_aware(datetime.combine(aula.data, aula.horario_fim))

    resposta = []

    for aluno in alunos:
        uid = aluno.uid 

        registros = (
            Presenca.objects
            .filter(uid=uid, horario__range=(inicio, fim))
            .order_by("horario")
        )

        presente = False

        if registros.exists():
            ultimo = registros.last()
            if ultimo.tipo == "IN":
                presente = True

        resposta.append({
            "aluno_id": aluno.id,
            "aluno_nome": aluno.nome,
            "presente": presente,
        })

    return JsonResponse({"presencas": resposta})