from django.urls import path
from .views import DisciplinaListView, DisciplinaCreateView, DisciplinaUpdateView, DisciplinaDeleteView
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

]