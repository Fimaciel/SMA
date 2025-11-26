from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Horarios 

class HorarioListView(ListView):
    model = Horarios
    template_name = "horario/horario_list.html"
    context_object_name = "horarios"


class HorarioCreateView(CreateView):
    model = Horarios
    fields = "__all__"
    template_name = "horario/horario_form.html"
    success_url = reverse_lazy("horario:list")


class HorarioUpdateView(UpdateView):
    model = Horarios
    fields = "__all__"
    template_name = "horario/horario_form.html"
    success_url = reverse_lazy("horario:list")


class HorarioDeleteView(DeleteView):
    model = Horarios
    template_name = "horario/horario_confirm_delete.html"
    success_url = reverse_lazy("horario:list")
