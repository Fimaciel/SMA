from django.urls import path
from .views import DisciplinaListView, DisciplinaCreateView, DisciplinaUpdateView, DisciplinaDeleteView

app_name = 'disciplina'

urlpatterns = [
    path('', DisciplinaListView.as_view(), name='disciplina_list'),
    path('add/', DisciplinaCreateView.as_view(), name='disciplina_add'),
    path('<int:pk>/edit/', DisciplinaUpdateView.as_view(), name='disciplina_edit'),
    path('<int:pk>/delete/', DisciplinaDeleteView.as_view(), name='disciplina_delete'),
]