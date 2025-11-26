from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Professor, ProfessorDisciplina
from .forms import ProfessorForm

class ProfessorListView(ListView):
    model = Professor
    template_name = 'professor/professor_list.html'
    context_object_name = 'professores'
    paginate_by = 10

class ProfessorCreateView(CreateView):
    model = Professor
    form_class = ProfessorForm
    template_name = 'professor/professor_form.html'
    success_url = reverse_lazy('professor:professor_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        disciplinas = form.cleaned_data.get('disciplinas')
        if disciplinas:
            self.object.professordisciplina_set.all().delete()
            for disciplina in disciplinas:
                ProfessorDisciplina.objects.create(professor=self.object, disciplina=disciplina)
        return response

class ProfessorUpdateView(UpdateView):
    model = Professor
    form_class = ProfessorForm
    template_name = 'professor/professor_form.html'
    success_url = reverse_lazy('professor:professor_list')

    def get_initial(self):
        initial = super().get_initial()
        initial['disciplinas'] = self.object.professordisciplina_set.values_list('disciplina_id', flat=True)
        return initial

    def form_valid(self, form):
        response = super().form_valid(form)
        disciplinas = form.cleaned_data.get('disciplinas')
        if disciplinas:
            self.object.professordisciplina_set.all().delete()
            for disciplina in disciplinas:
                ProfessorDisciplina.objects.create(professor=self.object, disciplina=disciplina)
        return response

class ProfessorDeleteView(DeleteView):
    model = Professor
    template_name = 'professor/professor_confirm_delete.html'
    success_url = reverse_lazy('professor:professor_list')
