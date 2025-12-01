import json
from django.utils import timezone
from datetime import datetime as dt
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Disciplina, Aula
from .forms import DisciplinaForm, AulaForm
from django.http import JsonResponse
from apps.presenca.models import PresencaAluno, RegistroRFID as Presenca
from django.utils.timezone import make_aware, datetime, now
from django.views.decorators.csrf import csrf_exempt


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

class AulaEncerradaView(DetailView):
    model = Aula
    template_name = "aula/aula_encerrada.html"
    context_object_name = "aula"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        aula = self.object
        presencas = PresencaAluno.objects.filter(aula=aula).select_related("aluno")

        lista_alunos = []

        for p in presencas:
            # tempo total formatado
            horas = int(p.tempo_total // 3600)
            minutos = int((p.tempo_total % 3600) // 60)
            segundos = int(p.tempo_total % 60)

            tempo_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"

            lista_alunos.append({
                "nome": p.aluno.nome,
                "presente": p.presente,
                "tempo_total": tempo_formatado,
            })

        context["presencas"] = lista_alunos

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



@csrf_exempt
def encerrar_aula(request, pk):
    aula = get_object_or_404(Aula, pk=pk)
    agora = timezone.localtime()

    tempo_front = 0
    if request.body:
        try:
            data = json.loads(request.body)
            tempo_front = int(data.get("tempo_decorrido", 0))
        except:
            tempo_front = 0

    # Caso o contador não seja enviado, calcular normalmente
    inicio_dt = timezone.make_aware(datetime.combine(aula.data, aula.horario_inicio))
    
    # Se horário_fim não existir, usa o tempo atual
    if aula.horario_fim is None:
        aula.horario_fim = agora.time()

    fim_dt = timezone.make_aware(datetime.combine(aula.data, aula.horario_fim))

    if fim_dt < inicio_dt:
        fim_dt = agora

    duracao_seg_backend = (fim_dt - inicio_dt).total_seconds()

    if tempo_front > 0:
        duracao_seg = tempo_front
    else:
        duracao_seg = duracao_seg_backend

    aula.tempo_total = int(duracao_seg)
    aula.encerrada = True
    aula.save()


    disciplina = aula.disciplina
    alunos = disciplina.alunos.all()

    duracao_min = duracao_seg / 60

    if duracao_min > 30:
        minimo = 0.75
    elif 20 <= duracao_min <= 30:
        minimo = 0.70
    else:
        minimo = 0.51

    for aluno in alunos:
        uid = getattr(aluno, "uid", None)
        tempo_total = 0
        presente = False

        if uid:
            registros = Presenca.objects.filter(
                uid=uid,
                horario__date=aula.data
            ).order_by("horario")

            ultima_entrada = None

            for r in registros:
                if r.tipo == "IN":
                    ultima_entrada = r.horario
                elif r.tipo == "OUT" and ultima_entrada:
                    tempo_total += (r.horario - ultima_entrada).total_seconds()
                    ultima_entrada = None

            if ultima_entrada:
                tempo_total += (agora - ultima_entrada).total_seconds()

            presente = tempo_total >= duracao_seg * minimo

        presenca, created = PresencaAluno.objects.get_or_create(
            aula=aula,
            aluno=aluno,
            defaults={
                "tempo_total": int(tempo_total),
                "presente": presente,
                "horario_entrada": None,
                "horario_saida": agora,
            }
        )

        if not created:
            presenca.tempo_total = int(tempo_total)
            presenca.presente = presente
            presenca.horario_saida = agora
            presenca.save()

    return JsonResponse({"aula_encerrada": True})

def aula_encerrada(request, pk):
    aula = get_object_or_404(Aula, pk=pk)
    alunos = aula.disciplina.alunos.all()

    presencas = []

    for aluno in alunos:
        registro = PresencaAluno.objects.filter(aula=aula, aluno=aluno).first()
        presente = registro.presente if registro else False

        presencas.append({
            "aluno": aluno,
            "presente": presente
        })

    context = {
        "aula": aula,
        "presencas": presencas,
    }

    return render(request, "aula/aula_encerrada.html", context)