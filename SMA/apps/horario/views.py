from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Horarios
from .forms import HorarioForm

class HorarioListView(ListView):
    model = Horarios
    template_name = 'horario/horario_list.html'
    context_object_name = 'horarios'
    paginate_by = 10

class HorarioCreateView(CreateView):
    model = Horarios
    form_class = HorarioForm
    template_name = 'horario/horario_form.html'
    success_url = reverse_lazy('horario:horario_list')

    def form_valid(self, form):
        # The M2M relationship can only be saved after the primary object is saved.
        self.object = form.save(commit=False)
        self.object.save()
        form.save_m2m() # Save the Many-to-Many relationship
        return super().form_valid(form)

class HorarioUpdateView(UpdateView):
    model = Horarios
    form_class = HorarioForm
    template_name = 'horario/horario_form.html'
    success_url = reverse_lazy('horario:horario_list')

    def form_valid(self, form):
        # The M2M relationship can only be saved after the primary object is saved.
        self.object = form.save(commit=False)
        self.object.save()
        form.save_m2m() # Save the Many-to-Many relationship
        return super().form_valid(form)

class HorarioDeleteView(DeleteView):
    model = Horarios
    template_name = 'horario/horario_confirm_delete.html'
    success_url = reverse_lazy('horario:horario_list')
