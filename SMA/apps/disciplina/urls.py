from django.urls import path
from .views import AulaEncerradaView, DisciplinaListView, DisciplinaCreateView, DisciplinaUpdateView, DisciplinaDeleteView, AulaView, aula_encerrada, encerrar_aula, presencas_json
from .views import (
    AulaListView,
    AulaCreateView,
    AulaUpdateView,
    AulaDeleteView,
)

app_name = 'disciplina'

urlpatterns = [
    path('', DisciplinaListView.as_view(), name='disciplina_list'),
    path('add/', DisciplinaCreateView.as_view(), name='disciplina_add'),
    path('<int:pk>/edit/', DisciplinaUpdateView.as_view(), name='disciplina_edit'),
    path('<int:pk>/delete/', DisciplinaDeleteView.as_view(), name='disciplina_delete'),
    path("aulas/", AulaListView.as_view(), name="aula_list"),
    path("aulas/add/", AulaCreateView.as_view(), name="aula_add"),
    path("aulas/<int:pk>/edit/", AulaUpdateView.as_view(), name="aula_edit"),
    path("aulas/<int:pk>/delete/", AulaDeleteView.as_view(), name="aula_delete"),
    path("aulas/<int:pk>/view/", AulaView.as_view(), name="aula_view"),
    path("aula/<int:pk>/presencas-json/", presencas_json, name="presencas_json"),
    path("aula/<int:pk>/encerrada/", AulaEncerradaView.as_view(), name="aula_encerrada"),
    path("aula/<int:pk>/encerrar/", encerrar_aula, name="encerrar_aula"),
    path("aula/<int:pk>/encerrada/", aula_encerrada, name="aula_encerrada"),
]